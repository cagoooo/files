# 手作課作品上傳平台 — 開發進度與未來規劃

> **目前版本**：v2.1
> **最後更新**：2026-03-18
> **GitHub**：https://github.com/cagoooo/files
> **線上版**：https://cagoooo.github.io/files/

---

## 零、版本紀錄

| 版本 | 日期 | 說明 |
|------|------|------|
| **v2.1** | 2026-03-18 | 加入石門信箱登入導向機制、預填 `@mail2.smes.tyc.edu.tw` 網域、登入提示 UI |
| **v2.0** | 2026-03-18 | 全面 UI/UX 優化、Fredoka + Nunito 字體、載入動畫、IntersectionObserver、PROGRESS.md |
| **v1.0** | 2026-03-18 | 初始版本：6 班級 Google Drive 串接、RWD 響應式、基礎 UI |

---

## 一、已完成項目 ✅

| # | 項目 | 版本 | 說明 |
|---|------|------|------|
| 1 | **基礎網站架構** | v1.0 | HTML5 + CSS3 + Vanilla JS，純靜態網站 |
| 2 | **Google Drive 串接** | v1.0 | 6 個班級（601-606）各自串接獨立的 Google Drive 資料夾 |
| 3 | **Google Drive 資料夾 ID 設定** | v1.0 | 所有 6 個班級的真實 folder ID 已配置在 `js/config.js` |
| 4 | **班級卡片 UI** | v2.0 | 6 色漸層卡片，hover 動效（位移、縮放、光暈、shimmer） |
| 5 | **RWD 響應式設計** | v1.0 | 桌面 3 欄 / 平板 2 欄 / 手機 1 欄，含行動版漢堡選單 |
| 6 | **導覽列 (Navbar)** | v2.0 | 固定頂部、毛玻璃效果、捲動時陰影變化、行動版選單 |
| 7 | **主視覺 Hero 區** | v2.0 | 全螢幕漸層背景、漂浮手作元素動畫、統計數據、雙按鈕 CTA |
| 8 | **使用說明區** | v2.0 | 時間軸三步驟設計、注意事項清單（含 SVG 圖示） |
| 9 | **聯絡資訊區** | v2.0 | 漸層卡片、裝飾圓形、email 連結 |
| 10 | **SVG Favicon** | v2.0 | 三色漸層「作」字圖示，配上傳箭頭 |
| 11 | **社群分享預覽圖 (OG Image)** | v2.0 | 1200x630 SVG，支援 FB/LINE/Twitter 分享卡片 |
| 12 | **Open Graph / Twitter / LINE Meta Tags** | v2.0 | 完整的 OG 標籤含絕對路徑 |
| 13 | **Google Fonts 字體** | v2.0 | Fredoka（標題）+ Nunito（內文），Playful Creative 風格 |
| 14 | **捲動進場動畫** | v2.0 | IntersectionObserver 實作，含交錯延遲效果 |
| 15 | **回到頂端按鈕** | v2.0 | 捲動顯示/隱藏，平滑回頂 |
| 16 | **載入動畫 (Loader)** | v2.0 | 彈跳剪刀+調色盤圖示，進度條動畫 |
| 17 | **無障礙 (Accessibility)** | v2.0 | ARIA 標籤、role 屬性、focus-visible、ESC 關閉 Modal、keyboard nav |
| 18 | **Reduced Motion** | v2.0 | `prefers-reduced-motion` 媒體查詢支援 |
| 19 | **未設定提示 Modal** | v1.0 | 當 folder ID 未設定時顯示引導彈窗 |
| 20 | **GitHub 推送** | v1.0 | 已推送至 `https://github.com/cagoooo/files` |
| 21 | **GitHub Pages 準備** | v2.0 | 結構已就緒，OG image 使用絕對路徑 |
| 22 | **README 文件** | v2.1 | 含設定教學、登入機制說明、版本紀錄、檔案結構 |
| 23 | **列印樣式** | v2.0 | `@media print` 隱藏不必要元素 |
| 24 | **UI/UX Pro Max 參考** | v2.0 | 已參考色彩、字體、無障礙、教育類 UI 設計建議 |
| 25 | **石門信箱登入導向** | v2.1 | 點擊上傳→自動跳轉 Google 登入→預填 `@mail2.smes.tyc.edu.tw` |
| 26 | **學校信箱網域設定** | v2.1 | `config.js` 可自訂 `SCHOOL_EMAIL_DOMAIN`，全站自動套用 |
| 27 | **登入提示 UI** | v2.1 | 班級專區顯示橘色信箱網域提示 badge |
| 28 | **使用說明更新** | v2.1 | 步驟 2 更新為「登入石門信箱」，注意事項更新對應文字 |

---

## 二、待啟用 / 需手動完成 ⚠️

| # | 項目 | 優先級 | 說明 |
|---|------|--------|------|
| 1 | **啟用 GitHub Pages** | 🔴 高 | 到 GitHub Settings → Pages → Deploy from branch (main) → Save |
| 2 | **OG Image 轉 PNG 格式** | 🟡 中 | 多數社群平台不支援 SVG 作為 OG Image，建議轉為 PNG 後替換 |
| 3 | **Google Drive 資料夾權限** | 🔴 高 | 需確認每個 Drive 資料夾已將 `@mail2.smes.tyc.edu.tw` 學生帳號加為編輯者 |
| 4 | **更新聯絡 Email** | 🟡 中 | 將 `teacher@school.edu.tw` 替換為真實 email |

---

## 三、未來優化改良建議 🚀

### 第一優先級（🔴 高）— 建議盡快實作

#### 3.1 OG Image PNG 化
**為什麼**：LINE、Facebook 等社群平台的爬蟲不支援 SVG 格式的 OG image，導致分享時可能不顯示預覽圖。
**怎麼做**：
- 方案 A：使用線上工具（如 svgtopng.com）將 `images/og-image.svg` 轉成 `images/og-image.png`
- 方案 B：使用 Python script 產生 PNG（需安裝 cairosvg）
- 更新 `index.html` 中的 `og:image` meta tag 路徑

#### 3.2 新增 PWA 支援（漸進式 Web App）
**為什麼**：學生可以「加到主畫面」，像原生 APP 一樣快速開啟。
**怎麼做**：
- 建立 `manifest.json`（含名稱、圖示、主題色）
- 建立 `sw.js`（Service Worker，離線快取）
- 在 `index.html` 加入 `<link rel="manifest">`
- 產生多尺寸 PNG icon（192x192, 512x512）

#### 3.3 班級密碼保護（簡易版）
**為什麼**：防止學生誤點進入其他班級的 Drive 資料夾。
**怎麼做**：
- 點擊「上傳作品」時跳出密碼輸入框
- 密碼存在 `config.js`（簡易方案，非高安全性）
- 密碼正確才開啟 Google Drive 連結
- 可搭配 sessionStorage 記住已驗證狀態

---

### 第二優先級（🟡 中）— 體驗提升

#### 3.4 深色模式（Dark Mode）
**怎麼做**：
- 增加 `prefers-color-scheme: dark` 媒體查詢
- 新增 CSS 變數的 dark mode 版本
- 可加入手動切換按鈕在 navbar

#### 3.5 多語言支援（i18n）
**怎麼做**：
- 建立 `js/i18n.js`，含中文/英文語言包
- 使用 `data-i18n` 屬性標記可翻譯元素
- 加入語言切換按鈕

#### 3.6 作品展示牆（Gallery）
**為什麼**：讓學生可以瀏覽已上傳的優秀作品，增加成就感。
**怎麼做**：
- 新增 Gallery section
- 使用 Google Drive API 讀取資料夾內圖片（需 API Key）
- 燈箱效果瀏覽圖片
- 瀑布流 / Masonry 排版

#### 3.7 上傳進度提示 Toast
**怎麼做**：
- 當使用者點擊「上傳作品」開啟新分頁後
- 顯示浮動提示「已開啟 Google Drive，請在新分頁中上傳檔案」
- 3 秒後自動消失

#### 3.8 班級公告 / 最新消息
**怎麼做**：
- 在 Hero 區下方加入跑馬燈或公告區塊
- 可透過 `config.js` 或 JSON 設定公告內容
- 支援標記為「新」「重要」「截止日」

---

### 第三優先級（🟢 低）— 進階功能

#### 3.9 Google Sheets 作為後端
**為什麼**：不需架設伺服器也能記錄上傳日誌。
**怎麼做**：
- 建立 Google Sheets 表單
- 使用 Google Apps Script 建立 Web API
- 每次點擊「上傳作品」時呼叫 API 記錄（班級、時間）
- 老師可在 Google Sheets 查看各班使用統計

#### 3.10 QR Code 產生器
**為什麼**：老師可以列印 QR Code 發給學生，掃碼即達。
**怎麼做**：
- 加入 QR Code 產生功能（使用 qrcode.js 套件）
- 每個班級產生獨立 QR Code
- 支援列印/下載 QR Code

#### 3.11 倒數計時器
**為什麼**：提醒學生上傳截止時間。
**怎麼做**：
- 在 `config.js` 設定截止日期
- Hero 區或班級卡片顯示倒數（天:時:分:秒）
- 過期後自動隱藏上傳按鈕或顯示「已截止」

#### 3.12 自訂主題色彩
**怎麼做**：
- 在 `config.js` 加入 theme 設定
- 支援多組主題：校慶版、聖誕版、母親節版等
- 自動套用不同的配色方案和裝飾元素

#### 3.13 Google Analytics 追蹤
**怎麼做**：
- 加入 GA4 tracking code
- 追蹤各班點擊次數
- 可在 GA 後台查看使用數據

#### 3.14 作品命名檢查器
**為什麼**：提醒學生按照正確格式命名檔案。
**怎麼做**：
- 在跳轉 Drive 前顯示命名格式提醒
- 或提供互動式命名產生器（選擇座號+輸入姓名+作品名稱）

#### 3.15 LINE Notify 通知
**怎麼做**：
- 串接 LINE Notify API
- 學生上傳作品後自動發送通知到老師的 LINE
- 需架設簡易 serverless function（可用 Cloudflare Workers 或 Vercel）

---

## 四、技術改進建議 🔧

| 項目 | 說明 |
|------|------|
| **CSS 最小化** | 部署前使用 cssnano 或線上工具壓縮 CSS |
| **HTML 最小化** | 使用 html-minifier 壓縮 HTML |
| **圖片最佳化** | 將 SVG favicon 轉為多尺寸 PNG（16/32/180/192/512）|
| **CDN 加速** | 考慮使用 Cloudflare 免費方案加速 GitHub Pages |
| **自訂網域** | 購買自訂域名（如 craft.school.edu.tw）指向 GitHub Pages |
| **SEO 優化** | 加入 sitemap.xml、robots.txt |
| **效能監控** | 使用 Lighthouse 跑分並持續優化（目標 90+） |
| **版本管理** | 使用語意化版號（v1.0.0, v1.1.0...）搭配 GitHub Releases |

---

## 五、設計系統參考 🎨

本專案 UI/UX 設計參考了 **UI UX Pro Max** 工具的建議：

| 面向 | 選擇 | 來源 |
|------|------|------|
| **字體配對** | Fredoka（標題）+ Nunito（內文） | Typography → Playful Creative |
| **色彩方案** | Indigo #4F46E5 + Orange #F97316 | Color → Educational App |
| **設計風格** | Inclusive Design + Accessible & Ethical | Style → Education 類 |
| **無障礙** | WCAG AA 等級，focus-visible, ARIA, reduced motion | Style → Accessible & Ethical |
| **觸控目標** | 最小 44x44px | UX → Touch Target Guidelines |

---

## 六、檔案結構

```
files/
├── index.html              # 主頁面 (HTML5 語意化標籤)
├── css/
│   └── style.css           # 樣式表 (CSS Variables + RWD)
├── js/
│   ├── config.js           # Google Drive 資料夾 ID + 學校信箱網域設定
│   └── main.js             # 互動功能 (含登入導向機制)
├── images/
│   ├── favicon.svg         # 網站圖示 (三色漸層「作」字)
│   └── og-image.svg        # 社群分享預覽圖 (1200x630)
├── .gitignore
├── README.md               # 設定教學 + 登入機制說明 + 版本紀錄
└── PROGRESS.md             # 本進度追蹤文件
```

---

## 七、部署 Checklist

- [x] Google Drive 6 個班級資料夾 ID 已設定
- [x] 石門信箱登入導向機制已實作
- [x] 學校信箱網域 `@mail2.smes.tyc.edu.tw` 已設定
- [x] 程式碼已推送至 GitHub（v2.1，共 3 個 commits）
- [x] README.md 含完整版本紀錄與登入機制說明
- [ ] 啟用 GitHub Pages（Settings → Pages → main branch）
- [ ] 確認 Google Drive 各資料夾已將學校帳號加為編輯者
- [ ] 將 OG image 轉為 PNG 格式
- [ ] 更新聯絡 Email 為真實地址
- [ ] 使用 Lighthouse 檢測效能分數
- [ ] 在 LINE/FB 分享連結測試預覽卡片
- [ ] 在手機瀏覽器測試 RWD 顯示
