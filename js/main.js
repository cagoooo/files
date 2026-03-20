/**
 * 手作課照片影片素材上傳平台 - 主程式 v3.2
 * Features: Google Drive integration, scroll animations,
 *           loader, back-to-top, mobile nav, accessibility,
 *           Toast notifications, QR Code generator, GA4 tracking,
 *           中繼頁防 App 跳轉機制
 */

// ========== GA4 自訂事件追蹤 ==========
function trackEvent(eventName, params) {
    if (typeof gtag === "function") {
        gtag("event", eventName, params || {});
    }
}

// ========== Loader ==========
window.addEventListener("load", function () {
    var loader = document.getElementById("loader");
    if (loader) {
        setTimeout(function () {
            loader.classList.add("hidden");
        }, 1400);
    }
    handleScrollAnimations();
});

// ========== Google Drive（中繼頁防 App 跳轉） ==========
/**
 * 開啟 Google Drive 資料夾
 *
 * 流程（v3.2.1 修正）：
 * 1. 先開啟中繼頁 go.html（在新分頁中，留在瀏覽器）
 * 2. 中繼頁顯示班級資訊 + 提供「登入石門信箱」按鈕
 * 3. 按鈕觸發 Google 登入（continue 指向 drive.google.com，Google 接受）
 * 4. 登入成功 → 在同一分頁中開啟 Drive（不跳 App）
 *
 * 為什麼不直接把 continue 指向 go.html？
 * → Google 的 continue 參數只接受 Google 網域，第三方 URL 會回 400 錯誤
 *
 * 為什麼先開中繼頁？
 * → 在瀏覽器分頁內用 location.replace 觸發的導航，
 *   不容易被手機 OS 攔截跳轉至 App
 */
function openDriveFolder(element, event) {
    event.preventDefault();
    var folderKey = element.getAttribute("data-folder");
    var folderId = DRIVE_CONFIG[folderKey];

    if (!folderId || folderId === "YOUR_FOLDER_ID_HERE") {
        document.getElementById("configModal").style.display = "flex";
        document.getElementById("configModal").querySelector(".modal-close-btn").focus();
        return;
    }

    // 取得班級編號
    var card = element.closest(".class-card");
    var classNum = card ? card.getAttribute("data-class") : "0";
    var classCode = "60" + classNum;

    // 直接開啟中繼頁（不經由 Google 登入，避免 400 錯誤）
    var baseUrl = window.location.href.replace(/[?#].*$/, "").replace(/\/[^/]*$/, "/");
    var goUrl = baseUrl + "go.html?folder=" + encodeURIComponent(folderId) + "&class=" + classCode;

    window.open(goUrl, "_blank", "noopener,noreferrer");

    // GA4: 追蹤上傳點擊
    trackEvent("upload_click", {
        class_number: classNum,
        class_name: classCode
    });

    // 顯示 Toast 通知
    showToast();
}

function closeModal() {
    document.getElementById("configModal").style.display = "none";
}

// Click overlay to close modal
document.addEventListener("click", function (e) {
    if (e.target.classList.contains("modal-overlay")) {
        closeModal();
    }
});

// ESC to close modal
document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
        closeModal();
    }
});

// ========== Mobile Nav ==========
var navToggle = document.getElementById("navToggle");
var navLinks = document.getElementById("navLinks");

if (navToggle && navLinks) {
    navToggle.addEventListener("click", function () {
        var isOpen = navLinks.classList.toggle("active");
        navToggle.classList.toggle("active");
        navToggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });

    // Close nav when clicking a link
    navLinks.querySelectorAll(".nav-link").forEach(function (link) {
        link.addEventListener("click", function () {
            navLinks.classList.remove("active");
            navToggle.classList.remove("active");
            navToggle.setAttribute("aria-expanded", "false");
        });
    });
}

// ========== Navbar Scroll Effect ==========
var lastScrollY = 0;

window.addEventListener("scroll", function () {
    var navbar = document.querySelector(".navbar");
    var scrollY = window.scrollY;

    if (scrollY > 20) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }

    lastScrollY = scrollY;
}, { passive: true });

// ========== Back to Top ==========
var backToTop = document.getElementById("backToTop");

window.addEventListener("scroll", function () {
    if (backToTop) {
        if (window.scrollY > 600) {
            backToTop.classList.add("visible");
        } else {
            backToTop.classList.remove("visible");
        }
    }
}, { passive: true });

if (backToTop) {
    backToTop.addEventListener("click", function () {
        window.scrollTo({ top: 0, behavior: "smooth" });
    });
}

// ========== Scroll Animations (Intersection Observer) ==========
function handleScrollAnimations() {
    var targets = document.querySelectorAll(
        ".class-card, .step-card, .tips-box"
    );

    if ("IntersectionObserver" in window) {
        var observer = new IntersectionObserver(
            function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add("visible");
                        observer.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.1, rootMargin: "0px 0px -60px 0px" }
        );

        targets.forEach(function (el) {
            observer.observe(el);
        });
    } else {
        // Fallback for older browsers
        targets.forEach(function (el) {
            el.classList.add("visible");
        });
    }
}

// ========== Smooth scroll for anchor links ==========
document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener("click", function (e) {
        var targetId = this.getAttribute("href");
        if (targetId === "#") return;

        var target = document.querySelector(targetId);
        if (target) {
            e.preventDefault();
            var offset = 80; // navbar height
            var top = target.getBoundingClientRect().top + window.pageYOffset - offset;
            window.scrollTo({ top: top, behavior: "smooth" });
        }
    });
});

// ========== Toast 通知 ==========
var toastTimer = null;

function showToast() {
    var toast = document.getElementById("toast");
    if (!toast) return;

    // 清除之前的計時器
    if (toastTimer) clearTimeout(toastTimer);

    toast.classList.add("visible");
    toastTimer = setTimeout(function () {
        toast.classList.remove("visible");
    }, 4000);
}

// ========== QR Code 功能 ==========
var currentQRClassName = "";

function showQRCode(btn) {
    // 找到同一卡片中的上傳按鈕取得 folder key
    var card = btn.closest(".class-card");
    if (!card) return;

    var classNum = card.getAttribute("data-class");
    var folderKey = "CLASS_" + classNum + "_FOLDER_ID";
    var folderId = DRIVE_CONFIG[folderKey];

    if (!folderId || folderId === "YOUR_FOLDER_ID_HERE") return;

    var classNames = {
        "1": "六年一班 (601)",
        "2": "六年二班 (602)",
        "3": "六年三班 (603)",
        "4": "六年四班 (604)",
        "5": "六年五班 (605)",
        "6": "六年六班 (606)"
    };

    currentQRClassName = classNames[classNum] || "班級 " + classNum;

    // QR Code 直接指向中繼頁（掃碼後在瀏覽器中開啟）
    var classCode = "60" + classNum;
    var baseUrl = window.location.href.replace(/[?#].*$/, "").replace(/\/[^/]*$/, "/");
    var loginUrl = baseUrl + "go.html?folder=" + encodeURIComponent(folderId) + "&class=" + classCode;

    // 產生 QR Code
    var qrCanvas = document.getElementById("qrCanvas");
    qrCanvas.innerHTML = "";

    if (typeof qrcode !== "undefined") {
        var qr = qrcode(0, "M");
        qr.addData(loginUrl);
        qr.make();
        qrCanvas.innerHTML = qr.createSvgTag({ cellSize: 5, margin: 4, scalable: true });

        // 設定 SVG 樣式
        var svg = qrCanvas.querySelector("svg");
        if (svg) {
            svg.style.width = "220px";
            svg.style.height = "220px";
            svg.style.maxWidth = "100%";
        }
    }

    // 更新班級名稱
    document.getElementById("qrClassName").textContent = currentQRClassName;
    document.getElementById("qrModalTitle").textContent = currentQRClassName + " QR Code";

    // 顯示 Modal
    document.getElementById("qrModal").style.display = "flex";

    // GA4: 追蹤 QR Code 檢視
    trackEvent("qr_code_view", {
        class_number: classNum,
        class_name: currentQRClassName
    });
}

function closeQRModal() {
    document.getElementById("qrModal").style.display = "none";
}

function downloadQR() {
    var svg = document.querySelector("#qrCanvas svg");
    if (!svg) return;

    // 將 SVG 轉為圖片下載
    var svgData = new XMLSerializer().serializeToString(svg);
    var canvas = document.createElement("canvas");
    canvas.width = 600;
    canvas.height = 600;
    var ctx = canvas.getContext("2d");

    // 白色背景
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, 600, 600);

    var img = new Image();
    img.onload = function () {
        ctx.drawImage(img, 50, 30, 500, 500);

        // 加入班級名稱文字
        ctx.fillStyle = "#1E1B4B";
        ctx.font = "bold 28px sans-serif";
        ctx.textAlign = "center";
        ctx.fillText(currentQRClassName, 300, 575);

        // 下載
        var link = document.createElement("a");
        link.download = "QRCode_" + currentQRClassName.replace(/[^a-zA-Z0-9\u4e00-\u9fff]/g, "_") + ".png";
        link.href = canvas.toDataURL("image/png");
        link.click();

        // GA4: 追蹤 QR Code 下載
        trackEvent("qr_code_download", { class_name: currentQRClassName });
    };
    img.src = "data:image/svg+xml;base64," + btoa(unescape(encodeURIComponent(svgData)));
}

function printQR() {
    var svg = document.querySelector("#qrCanvas svg");
    if (!svg) return;

    var printWindow = window.open("", "_blank");
    printWindow.document.write(
        "<!DOCTYPE html><html><head><title>QR Code - " + currentQRClassName + "</title>" +
        "<style>body{display:flex;flex-direction:column;align-items:center;justify-content:center;" +
        "min-height:100vh;margin:0;font-family:sans-serif;}" +
        "h2{margin-bottom:20px;font-size:24px;color:#1E1B4B;}" +
        "svg{width:300px;height:300px;}" +
        "p{margin-top:16px;color:#475569;font-size:14px;}</style></head><body>" +
        "<h2>" + currentQRClassName + "</h2>" +
        new XMLSerializer().serializeToString(svg) +
        "<p>掃描 QR Code 即可上傳手作課照片影片素材</p>" +
        "<p style='color:#94A3B8;font-size:12px;'>手作課照片影片素材上傳平台 — Made with 💝 by 阿凱老師</p>" +
        "</body></html>"
    );
    printWindow.document.close();
    printWindow.onload = function () {
        printWindow.print();
    };
}

// ESC 關閉 QR Modal
document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
        closeQRModal();
    }
});
