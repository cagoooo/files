# 手作課作品上傳平台 — 開發進度與未來規劃

> **目前版本**：v3.1
> **最後更新**：2026-03-18
> **GitHub**：https://github.com/cagoooo/files
> **線上版**：https://cagoooo.github.io/files/

---

## 零、版本紀錄

| 版本 | 日期 | Commit | 說明 |
|------|------|--------|------|
| **v3.1** | 2026-03-18 | — | OG Image / PWA Icon PNG 化、GA4 追蹤整合、Lighthouse 效能優化（defer 腳本、cursor 無障礙） |
| **v3.0** | 2026-03-18 | `b608555` | Toast 上傳提示通知、PWA 支援（manifest.json + Service Worker）、QR Code 班級快捷（產生/下載/列印） |
| **v2.2** | 2026-03-18 | `9107f84` | 更新聯絡 Email 為 `ipad@mail2.smes.tyc.edu.tw`、Footer 加入「Made with 💝 by 阿凱老師」署名與學校超連結 |
| **v2.1** | 2026-03-18 | `eb42f33` | 加入石門信箱登入導向機制、Google 登入頁預填 `@mail2.smes.tyc.edu.tw` 網域、登入提示 UI |
| **v2.0** | 2026-03-18 | `fac6777` | 全面 UI/UX 優化、Fredoka + Nunito 字體、載入動畫、IntersectionObserver、PROGRESS.md |
| **v1.0** | 2026-03-18 | `f7b542e` | 初始版本：6 班級 Google Drive 串接、RWD 響應式、基礎 UI |

---

## 一、已完成項目 ✅（共 43 項）

### 核心功能

| # | 項目 | 版本 | 說明 |
|---|------|------|------|
| 1 | **基礎網站架構** | v1.0 | HTML5 + CSS3 + Vanilla JS，純靜態網站，可部署於 GitHub Pages |
| 2 | **Google Drive 串接** | v1.0 | 6 個班級（601-606）各自串接獨立的 Google Drive 資料夾 |
| 3 | **Google Drive 資料夾 ID 設定** | v1.0 | 所有 6 個班級的真實 folder ID 已配置在 `js/config.js` |
| 4 | **石門信箱登入導向** | v2.1 | 點擊上傳→自動跳轉 Google 登入→預填 `@mail2.smes.tyc.edu.tw` |
| 5 | **學校信箱網域設定** | v2.1 | `config.js` 可自訂 `SCHOOL_EMAIL_DOMAIN`，全站自動套用 |
| 6 | **未設定提示 Modal** | v1.0 | 當 folder ID 未設定時顯示引導彈窗，ESC 鍵可關閉 |
| 7 | **Toast 上傳提示通知** | v3.0 | 點擊「上傳作品」後底部浮動提示「已開啟 Google Drive，請在新分頁中上傳」，4 秒自動消失 |
| 8 | **QR Code 班級快捷** | v3.0 | 每張班級卡片「顯示 QR Code」按鈕，彈窗顯示含登入 URL 的 QR Code，支援下載 PNG / 列印 |

### UI/UX 設計

| # | 項目 | 版本 | 說明 |
|---|------|------|------|
| 9 | **班級卡片 UI** | v2.0 | 6 色漸層卡片，hover 動效（位移、縮放、光暈、shimmer） |
| 10 | **導覽列 (Navbar)** | v2.0 | 固定頂部、毛玻璃效果、捲動時陰影變化、行動版漢堡選單 |
| 11 | **主視覺 Hero 區** | v2.0 | 全螢幕漸層背景、漂浮手作元素動畫、統計數據、雙按鈕 CTA |
| 12 | **使用說明區** | v2.1 | 時間軸三步驟（選班級→登入石門信箱→上傳）、注意事項清單 |
| 13 | **聯絡資訊區** | v2.2 | 漸層卡片、裝飾圓形、真實 email 連結 `ipad@mail2.smes.tyc.edu.tw` |
| 14 | **登入提示 UI** | v2.1 | 班級專區顯示橘色信箱網域提示 badge |
| 15 | **Google Fonts 字體** | v2.0 | Fredoka（標題）+ Nunito（內文），Playful Creative 風格 |
| 16 | **載入動畫 (Loader)** | v2.0 | 彈跳剪刀+調色盤圖示，進度條動畫 |
| 17 | **捲動進場動畫** | v2.0 | IntersectionObserver 實作，含交錯延遲效果 |
| 18 | **回到頂端按鈕** | v2.0 | 捲動超過 600px 顯示，平滑回頂 |
| 19 | **捲動指示器** | v2.0 | Hero 區底部「往下滑動」動畫提示 |
| 20 | **QR Code Modal** | v3.0 | QR Code 彈窗含班級名稱標題、下載按鈕、列印按鈕、關閉 ESC 鍵盤支援 |

### RWD 響應式

| # | 項目 | 版本 | 說明 |
|---|------|------|------|
| 21 | **桌面版** | v1.0 | 3 欄班級卡片佈局（>1024px） |
| 22 | **平板版** | v1.0 | 2 欄佈局（768px-1024px） |
| 23 | **手機版** | v2.0 | 1 欄佈局（<480px）、漢堡選單、全寬按鈕 |

### 無障礙 & 效能

| # | 項目 | 版本 | 說明 |
|---|------|------|------|
| 24 | **ARIA 無障礙** | v2.0 | role、aria-label、aria-expanded、aria-hidden 屬性 |
| 25 | **鍵盤導覽** | v2.0 | focus-visible 焦點樣式、ESC 關閉 Modal |
| 26 | **Reduced Motion** | v2.0 | `prefers-reduced-motion` 媒體查詢，尊重使用者偏好 |
| 27 | **列印樣式** | v2.0 | `@media print` 隱藏不必要的裝飾元素 |

### PWA 漸進式 Web App

| # | 項目 | 版本 | 說明 |
|---|------|------|------|
| 28 | **Web App Manifest** | v3.0 | `manifest.json` 含名稱、圖示、主題色、啟動模式（standalone） |
| 29 | **Service Worker** | v3.0 | `sw.js` Network First 策略，預先快取核心資源，離線可看首頁 |
| 30 | **PWA Meta Tags** | v3.0 | `apple-mobile-web-app-capable`、`theme-color`、`<link rel="manifest">` |

### 品牌 & 社群

| # | 項目 | 版本 | 說明 |
|---|------|------|------|
| 31 | **SVG Favicon** | v2.0 | 三色漸層「作」字圖示，配上傳箭頭 |
| 32 | **Favicon PNG 多尺寸** | v3.1 | 16/32/180/192/512 px PNG，支援所有瀏覽器與 PWA |
| 33 | **社群預覽圖 (OG Image PNG)** | v3.1 | 1200x630 PNG，紫色漸層+中文標題+6 色圓點，LINE/FB 可正常顯示 |
| 34 | **OG / Twitter / LINE Meta** | v2.0 | 完整的 meta tags 含絕對路徑（`cagoooo.github.io`） |

### 數據追蹤

| # | 項目 | 版本 | 說明 |
|---|------|------|------|
| 35 | **GA4 追蹤整合** | v3.1 | `config.js` 設定 Measurement ID，自動載入 GA4，不硬編碼 |
| 36 | **GA4 自訂事件** | v3.1 | 追蹤 `upload_click`（含班級）、`qr_code_view`、`qr_code_download` |

### Lighthouse 效能優化

| # | 項目 | 版本 | 說明 |
|---|------|------|------|
| 37 | **Script defer 載入** | v3.1 | QR Code CDN、config.js、main.js 加入 `defer`，減少 render blocking |
| 38 | **互動元素 cursor** | v3.1 | 全域 `cursor: pointer` 規則，提升無障礙與 UX |
| 39 | **Service Worker 快取更新** | v3.1 | 快取版本升級至 v3.1，新增 PNG icon 預快取 |

### 部署 & 文件

| # | 項目 | 版本 | 說明 |
|---|------|------|------|
| 40 | **GitHub 推送** | v3.1 | 已推送至 `https://github.com/cagoooo/files` |
| 41 | **README 文件** | v3.1 | 含功能特色、設定教學、登入機制說明、版本紀錄 |
| 42 | **PROGRESS 進度文件** | v3.1 | 完整開發進度表與未來優化路線圖（本文件） |
| 43 | **Footer 署名** | v2.2 | 「Made with 💝 by 阿凱老師」含學校網站超連結（開新視窗） |

---

## 二、待啟用 / 需手動完成 ⚠️

| # | 項目 | 優先級 | 狀態 | 說明 |
|---|------|--------|------|------|
| 1 | ~~啟用 GitHub Pages~~ | — | ✅ 已完成 | Settings → Pages → Deploy from branch (main) → Save |
| 2 | ~~確認 Drive 資料夾權限~~ | — | ✅ 已完成 | `@mail2.smes.tyc.edu.tw` 學生帳號已可存取 |
| 3 | ~~OG Image 轉 PNG~~ | — | ✅ 已完成 | 1200x630 PNG，紫色漸層 + 中文標題（v3.1） |
| 4 | ~~PWA 圖示轉 PNG~~ | — | ✅ 已完成 | 192x192 + 512x512 + apple-touch-icon 180x180（v3.1） |
| 5 | **設定 GA4 Measurement ID** | 🟡 中 | ⬜ 待做 | 在 `config.js` 中填入真實的 GA4 ID（目前為佔位符） |
| 6 | **LINE/FB 分享測試** | 🟡 中 | ⬜ 待做 | 部署後在 LINE/FB 分享連結，確認預覽卡片正常 |
| 7 | **手機瀏覽器測試** | 🟡 中 | ⬜ 待做 | 在 iPhone/Android 實機測試 RWD、登入導向、PWA 安裝 |

---

## 三、未來優化改良建議 🚀

### ~~第一優先級~~ ✅ 已完成

> ✅ **3.1 OG Image & PWA Icon PNG 化** — v3.1 已用 Python + Pillow 產生所有尺寸 PNG
> ✅ **3.2 GA4 追蹤整合** — v3.1 已加入動態載入 + 自訂事件（upload_click / qr_code_view / qr_code_download）

---

### 第一優先級（🟡 中）— 體驗提升

#### 3.3 班級密碼保護（簡易版）
- **為什麼**：增加一層防護，避免學生誤點其他班級
- **怎麼做**：
  - 點擊「上傳作品」時跳出密碼輸入 Modal
  - 每班可設不同密碼，存在 `config.js`
  - 使用 `sessionStorage` 記住已驗證狀態（同一瀏覽階段不重複驗證）
  - 密碼正確 → 導向 Google 登入 → Drive 資料夾
- **預估工時**：30 分鐘
- **注意**：前端密碼為「防君子不防小人」，真正的安全靠 Google Drive 帳號權限

#### 3.4 深色模式（Dark Mode）
- **怎麼做**：
  - 新增 `:root[data-theme="dark"]` CSS 變數組
  - 自動偵測 `prefers-color-scheme: dark`
  - Navbar 加入🌙/☀️ 切換按鈕
  - `localStorage` 記住使用者偏好
- **預估工時**：45 分鐘

#### 3.5 班級公告 / 最新消息
- **怎麼做**：
  - Hero 區下方加入公告橫幅（Announcement Bar）
  - `config.js` 新增 `ANNOUNCEMENTS` 陣列，可設定：
    ```js
    ANNOUNCEMENTS: [
      { text: "本週五前請完成上傳！", type: "urgent", date: "2026-03-22" },
      { text: "新增影片上傳功能", type: "new" }
    ]
    ```
  - 支援標記：🔴 緊急 / 🆕 新功能 / 📅 截止日
  - 可設定顯示/隱藏
- **預估工時**：30 分鐘

#### 3.6 作品展示牆（Gallery）
- **為什麼**：展示優秀作品，增加學生成就感與學習動力
- **怎麼做**：
  - 新增 `#gallery` section
  - 使用 Google Drive API 讀取資料夾內圖片縮圖（需 API Key）
  - 瀑布流 / Masonry 排版
  - 燈箱效果點擊放大瀏覽
  - 可按班級篩選
- **預估工時**：2-3 小時（需申請 Google API Key）

#### 3.7 作品命名檢查器
- **為什麼**：確保學生上傳的檔案命名統一，方便老師整理
- **怎麼做**：
  - 跳轉 Drive 前顯示命名格式提醒彈窗
  - 提供互動式命名產生器（選座號+輸入姓名+作品名稱 → 自動組合）
  - 一鍵複製命名結果
- **預估工時**：30 分鐘

---

### 第三優先級（🟢 低）— 進階功能

#### 3.8 倒數計時器
- **用途**：提醒學生上傳截止時間
- `config.js` 設定截止日期 → Hero 區或卡片顯示倒數（天:時:分:秒）
- 過期後按鈕變灰+顯示「已截止」
- **預估工時**：25 分鐘

#### 3.9 Google Sheets 上傳日誌
- **用途**：不需架設伺服器也能記錄使用統計
- Google Sheets + Apps Script 建立 Web API
- 每次點擊「上傳作品」時記錄（班級、時間、UA）
- 老師在 Sheets 查看各班使用頻率
- **預估工時**：45 分鐘

#### 3.10 自訂主題色彩
- `config.js` 加入 `THEME` 設定
- 支援多組主題：預設版、校慶版、聖誕版、母親節版
- 自動套用不同配色、裝飾元素
- **預估工時**：1 小時

#### 3.11 LINE Notify 通知
- 串接 LINE Notify API
- 學生上傳後自動通知老師 LINE
- 需 serverless function（Cloudflare Workers / Vercel）
- **預估工時**：1-2 小時

#### 3.12 多語言支援（i18n）
- 建立 `js/i18n.js` 語言包（中文/英文）
- `data-i18n` 屬性標記可翻譯元素
- Navbar 加入語言切換按鈕
- **預估工時**：1 小時

#### 3.13 教學影片整合
- **為什麼**：學生可能不熟悉 Google Drive 操作
- **怎麼做**：
  - 錄製 1-2 分鐘操作教學影片
  - 上傳 YouTube 後嵌入使用說明區
  - 或用 GIF 動圖展示操作流程
- **預估工時**：30 分鐘（不含錄影）

#### 3.14 班級作品統計儀表板
- **為什麼**：老師可以即時掌握各班上傳進度
- **怎麼做**：
  - 使用 Google Drive API 統計各資料夾檔案數
  - 首頁顯示簡易進度條（如：601 已上傳 18/30）
  - 可選擇性顯示排行榜鼓勵上傳
- **預估工時**：2-3 小時（需 Google API Key）

---

## 四、技術改進建議 🔧

| 項目 | 說明 | 優先級 |
|------|------|--------|
| ~~OG Image PNG 化~~ | ✅ 已完成（v3.1） | — |
| ~~PWA Icon PNG 化~~ | ✅ 已完成（v3.1，含 apple-touch-icon） | — |
| **Favicon PNG 多尺寸** | 產生 16/32/180 px 的 PNG 給不同瀏覽器 | 🟡 中 |
| **Lighthouse 跑分** | 目標各項 90+，持續追蹤效能 | 🟡 中 |
| **CSS 壓縮** | 使用 cssnano 或線上工具壓縮 CSS（預估可減少 30%） | 🟢 低 |
| **HTML 壓縮** | 使用 html-minifier 移除註解和空白 | 🟢 低 |
| **CDN 加速** | Cloudflare 免費方案加速 GitHub Pages | 🟢 低 |
| **自訂網域** | 購買域名（如 `craft.smes.tyc.edu.tw`）指向 GitHub Pages | 🟢 低 |
| **SEO 優化** | 加入 `sitemap.xml`、`robots.txt` | 🟢 低 |
| **GitHub Releases** | 使用語意化版號 + GitHub Releases 管理版本 | 🟢 低 |
| **GitHub Actions CI** | 自動化 HTML/CSS 檢查、Lighthouse 分數監控 | 🟢 低 |

---

## 五、設計系統參考 🎨

本專案 UI/UX 設計參考了 **UI UX Pro Max** 工具的建議：

| 面向 | 選擇 | 來源 |
|------|------|------|
| **字體配對** | Fredoka（標題）+ Nunito（內文） | Typography → Playful Creative |
| **色彩方案** | Indigo `#4F46E5` + Orange `#F97316` | Color → Educational App |
| **設計風格** | Inclusive Design + Accessible & Ethical | Style → Education 類 |
| **無障礙** | WCAG AA 等級，focus-visible, ARIA, reduced motion | Style → Accessible & Ethical |
| **觸控目標** | 最小 44x44px | UX → Touch Target Guidelines |

---

## 六、檔案結構

```
files/
├── index.html              # 主頁面 (v3.1, HTML5 語意化標籤)
├── css/
│   └── style.css           # 樣式表 (CSS Variables + RWD + Toast + QR + cursor 優化)
├── js/
│   ├── config.js           # 設定檔 (Drive ID + 學校信箱 + GA4 ID)
│   └── main.js             # 互動功能 (v3.1, 登入導向 + Toast + QR + GA4 事件)
├── images/
│   ├── favicon.svg         # 網站圖示 SVG (三色漸層「作」字)
│   ├── favicon-16.png      # Favicon 16x16 PNG
│   ├── favicon-32.png      # Favicon 32x32 PNG
│   ├── favicon-512.png     # Favicon 512x512 PNG (來源)
│   ├── apple-touch-icon.png # Apple Touch Icon 180x180
│   ├── icon-192.png        # PWA 圖示 192x192 ✅
│   ├── icon-512.png        # PWA 圖示 512x512 ✅
│   ├── og-image.svg        # 社群預覽圖 SVG 原始檔
│   └── og-image.png        # 社群預覽圖 PNG 1200x630 ✅
├── manifest.json           # PWA Web App Manifest
├── sw.js                   # Service Worker (Network First, v3.1 快取)
├── tools/
│   ├── generate_images.py  # Favicon PNG 產生工具
│   └── generate_og.py      # OG Image PNG 產生工具
├── .gitignore
├── README.md               # 說明文件 (v3.1)
└── PROGRESS.md             # 本進度追蹤文件 (v3.1)
```

---

## 七、部署 Checklist

- [x] Google Drive 6 個班級資料夾 ID 已設定
- [x] 石門信箱登入導向機制已實作（`@mail2.smes.tyc.edu.tw`）
- [x] 聯絡 Email 已更新為 `ipad@mail2.smes.tyc.edu.tw`
- [x] Footer 已加入「Made with 💝 by 阿凱老師」+ 學校連結
- [x] Toast 上傳提示通知（點擊上傳後底部浮動提示）
- [x] PWA 支援（manifest.json + Service Worker）
- [x] QR Code 班級快捷（產生 / 下載 PNG / 列印）
- [x] OG Image PNG 化（1200x630 紫色漸層 + 中文標題）
- [x] PWA PNG 圖示（16/32/180/192/512 px 全尺寸）
- [x] GA4 追蹤整合（config.js 設定 + 自訂事件追蹤）
- [x] Lighthouse 優化（defer 腳本、cursor 無障礙、快取更新）
- [x] 啟用 GitHub Pages ✅
- [x] 確認 Google Drive 各資料夾權限 ✅
- [x] 程式碼已推送至 GitHub（v3.1）
- [x] README.md 含完整版本紀錄與登入機制說明
- [ ] 設定真實 GA4 Measurement ID（config.js）
- [ ] LINE/FB 分享連結測試預覽卡片
- [ ] Lighthouse 實際跑分驗證（目標 90+）
- [ ] 手機實機測試 RWD + 登入導向 + PWA 安裝

---

## 八、推薦實作順序 📋

已完成的批次以 ✅ 標記，接下來建議按順序進行：

```
第 1 批 ✅ 已完成（v2.1 ~ v2.2）
  ├── ✅ 石門信箱登入導向機制
  ├── ✅ Footer 署名 + 學校連結
  └── ✅ 聯絡 Email 更新

第 2 批 ✅ 已完成（v3.0）
  ├── ✅ Toast 上傳提示通知
  ├── ✅ PWA 支援（加到主畫面）
  └── ✅ QR Code 班級快捷

第 3 批 ✅ 已完成（v3.1）
  ├── ✅ OG Image + PWA Icon PNG 化
  ├── ✅ GA4 追蹤整合（需填入真實 ID）
  └── ✅ Lighthouse 效能優化

第 4 批 ── 接下來建議做（30-60 分鐘）
  ├── 📌 班級公告 / 最新消息
  ├── 📌 班級密碼保護
  ├── 📌 深色模式
  └── 📌 作品命名檢查器

第 5 批 ── 進階功能（需更多時間）
  ├── 📌 作品展示牆 Gallery
  ├── 📌 班級作品統計儀表板
  ├── 📌 Google Sheets 日誌
  ├── 📌 倒數計時器
  ├── 📌 教學影片整合
  └── 📌 LINE Notify 通知
```
