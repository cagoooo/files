/**
 * Service Worker — 手作課照片影片素材上傳平台 v3.2.3
 * 快取策略：Network First（優先網路，失敗時用快取）
 */

// 同網域（cagoooo.github.io）的其他工具也共用 Cache Storage，只能清除本工具自己的快取
var CACHE_PREFIX = "craft-upload-";
var CACHE_NAME = CACHE_PREFIX + "v3.2.3";
var ASSETS = [
    "./",
    "./index.html",
    "./go.html",
    "./css/style.css",
    "./js/config.js",
    "./js/main.js",
    "./images/favicon.svg",
    "./images/icon-192.png",
    "./manifest.json"
];

// Install: 預先快取核心資源
self.addEventListener("install", function (event) {
    event.waitUntil(
        caches.open(CACHE_NAME).then(function (cache) {
            return cache.addAll(ASSETS);
        })
    );
    self.skipWaiting();
});

// Activate: 清除舊版快取
self.addEventListener("activate", function (event) {
    event.waitUntil(
        caches.keys().then(function (names) {
            return Promise.all(
                names
                    .filter(function (name) { return name.indexOf(CACHE_PREFIX) === 0 && name !== CACHE_NAME; })
                    .map(function (name) { return caches.delete(name); })
            );
        })
    );
    self.clients.claim();
});

// Fetch: Network First 策略
self.addEventListener("fetch", function (event) {
    // 只處理 GET 請求
    if (event.request.method !== "GET") return;

    // 跳過外部資源（Google Fonts、CDN 等）
    if (!event.request.url.startsWith(self.location.origin)) return;

    event.respondWith(
        fetch(event.request)
            .then(function (response) {
                // 成功取得網路回應，更新快取
                var clone = response.clone();
                caches.open(CACHE_NAME).then(function (cache) {
                    cache.put(event.request, clone);
                });
                return response;
            })
            .catch(function () {
                // 網路失敗，使用快取
                return caches.match(event.request);
            })
    );
});
