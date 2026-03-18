# 手作課作品上傳平台 — 開發進度與未來規劃

> **目前版本**：v2.2
> **最後更新**：2026-03-18
> **GitHub**：https://github.com/cagoooo/files
> **線上版**：https://cagoooo.github.io/files/

---

## 零、版本紀錄

| 版本 | 日期 | Commit | 說明 |
|------|------|--------|------|
| **v2.2** | 2026-03-18 | `9107f84` | 更新聯絡 Email 為 `ipad@mail2.smes.tyc.edu.tw`、Footer 加入「Made with 💝 by 阿凱老師」署名與學校超連結 |
| **v2.1** | 2026-03-18 | `eb42f33` | 加入石門信箱登入導向機制、Google 登入頁預填 `@mail2.smes.tyc.edu.tw` 網域、登入提示 UI |
| **v2.0** | 2026-03-18 | `fac6777` | 全面 UI/UX 優化、Fredoka + Nunito 字體、載入動畫、IntersectionObserver、PROGRESS.md |
| **v1.0** | 2026-03-18 | `f7b542e` | 初始版本：6 班級 Google Drive 串接、RWD 響應式、基礎 UI |

---

## 一、已完成項目 ✅（共 31 項）

### 核心功能

| # | 項目 | 版本 | 說明 |
|---|------|------|------|
| 1 | **基礎網站架構** | v1.0 | HTML5 + CSS3 + Vanilla JS，純靜態網站，可部署於 GitHub Pages |
| 2 | **Google Drive 串接** | v1.0 | 6 個班級（601-606）各自串接獨立的 Google Drive 資料夾 |
| 3 | **Google Drive 資料夾 ID 設定** | v1.0 | 所有 6 個班級的真實 folder ID 已配置在 `js/config.js` |
| 4 | **石門信箱登入導向** | v2.1 | 點擊上傳→自動跳轉 Google 登入→預填 `@mail2.smes.tyc.edu.tw` |
| 5 | **學校信箱網域設定** | v2.1 | `config.js` 可自訂 `SCHOOL_EMAIL_DOMAIN`，全站自動套用 |
| 6 | **未設定提示 Modal** | v1.0 | 當 folder ID 未設定時顯示引導彈窗，ESC 鍵可關閉 |

### UI/UX 設計

| # | 項目 | 版本 | 說明 |
|---|------|------|------|
| 7 | **班級卡片 UI** | v2.0 | 6 色漸層卡片，hover 動效（位移、縮放、光暈、shimmer） |
| 8 | **導覽列 (Navbar)** | v2.0 | 固定頂部、毛玻璃效果、捲動時陰影變化、行動版漢堡選單 |
| 9 | **主視覺 Hero 區** | v2.0 | 全螢幕漸層背景、漂浮手作元素動畫、統計數據、雙按鈕 CTA |
| 10 | **使用說明區** | v2.1 | 時間軸三步驟（選班級→登入石門信箱→上傳）、注意事項清單 |
| 11 | **聯絡資訊區** | v2.2 | 漸層卡片、裝飾圓形、真實 email 連結 `ipad@mail2.smes.tyc.edu.tw` |
| 12 | **登入提示 UI** | v2.1 | 班級專區顯示橘色信箱網域提示 badge |
| 13 | **Google Fonts 字體** | v2.0 | Fredoka（標題）+ Nunito（內文），Playful Creative 風格 |
| 14 | **載入動畫 (Loader)** | v2.0 | 彈跳剪刀+調色盤圖示，進度條動畫 |
| 15 | **捲動進場動畫** | v2.0 | IntersectionObserver 實作，含交錯延遲效果 |
| 16 | **回到頂端按鈕** | v2.0 | 捲動超過 600px 顯示，平滑回頂 |
| 17 | **捲動指示器** | v2.0 | Hero 區底部「往下滑動」動畫提示 |

### RWD 響應式

| # | 項目 | 版本 | 說明 |
|---|------|------|------|
| 18 | **桌面版** | v1.0 | 3 欄班級卡片佈局（>1024px） |
| 19 | **平板版** | v1.0 | 2 欄佈局（768px-1024px） |
| 20 | **手機版** | v2.0 | 1 欄佈局（<480px）、漢堡選單、全寬按鈕 |

### 無障礙 & 效能

| # | 項目 | 版本 | 說明 |
|---|------|------|------|
| 21 | **ARIA 無障礙** | v2.0 | role、aria-label、aria-expanded、aria-hidden 屬性 |
| 22 | **鍵盤導覽** | v2.0 | focus-visible 焦點樣式、ESC 關閉 Modal |
| 23 | **Reduced Motion** | v2.0 | `prefers-reduced-motion` 媒體查詢，尊重使用者偏好 |
| 24 | **列印樣式** | v2.0 | `@media print` 隱藏不必要的裝飾元素 |

### 品牌 & 社群

| # | 項目 | 版本 | 說明 |
|---|------|------|------|
| 25 | **SVG Favicon** | v2.0 | 三色漸層「作」字圖示，配上傳箭頭 |
| 26 | **社群預覽圖 (OG Image)** | v2.0 | 1200x630 SVG，含 Logo、標題、6 色班級圓點 |
| 27 | **OG / Twitter / LINE Meta** | v2.0 | 完整的 meta tags 含絕對路徑（`cagoooo.github.io`） |

### 部署 & 文件

| # | 項目 | 版本 | 說明 |
|---|------|------|------|
| 28 | **GitHub 推送** | v1.0 | 已推送至 `https://github.com/cagoooo/files`（共 5 個 commits） |
| 29 | **README 文件** | v2.2 | 含功能特色、設定教學、登入機制說明、版本紀錄 |
| 30 | **PROGRESS 進度文件** | v2.2 | 完整開發進度表與未來優化路線圖（本文件） |
| 31 | **Footer 署名** | v2.2 | 「Made with 💝 by 阿凱老師」含學校網站超連結（開新視窗） |

---

## 二、待啟用 / 需手動完成 ⚠️

| # | 項目 | 優先級 | 狀態 | 說明 |
|---|------|--------|------|------|
| 1 | **啟用 GitHub Pages** | 🔴 高 | ⬜ 待做 | Settings → Pages → Deploy from branch (main) → Save |
| 2 | **確認 Drive 資料夾權限** | 🔴 高 | ⬜ 待做 | 確認 `@mail2.smes.tyc.edu.tw` 學生帳號可存取 |
| 3 | **OG Image 轉 PNG** | 🟡 中 | ⬜ 待做 | 社群平台不支援 SVG，需轉 PNG 並更新 meta tag |
| 4 | ~~更新聯絡 Email~~ | — | ✅ 已完成 | 已更新為 `ipad@mail2.smes.tyc.edu.tw`（v2.2） |
| 5 | **LINE/FB 分享測試** | 🟡 中 | ⬜ 待做 | 部署後在 LINE/FB 分享連結，確認預覽卡片正常 |
| 6 | **手機瀏覽器測試** | 🟡 中 | ⬜ 待做 | 在 iPhone/Android 實機測試 RWD 與登入導向 |

---

## 三、未來優化改良建議 🚀

### 第一優先級（🔴 高）— 建議盡快實作

#### 3.1 OG Image PNG 化
- **為什麼**：LINE、Facebook 的爬蟲不支援 SVG 格式，分享時不會顯示預覽圖
- **怎麼做**：
  - 方案 A：用線上工具（svgtopng.com）將 `images/og-image.svg` 轉成 PNG
  - 方案 B：用 Figma/Canva 重新製作 1200x630 的 PNG 預覽圖
  - 更新 `index.html` 中 `og:image` 路徑為 `.png`
- **預估工時**：10 分鐘

#### 3.2 PWA 漸進式 Web App
- **為什麼**：學生可以「加到主畫面」，像 APP 一樣一鍵開啟，不用記網址
- **怎麼做**：
  - 建立 `manifest.json`（名稱、圖示、主題色、啟動畫面）
  - 建立 `sw.js` Service Worker（快取 HTML/CSS/JS，離線可看首頁）
  - 在 `index.html` 加入 `<link rel="manifest">`
  - 產生多尺寸 PNG icon（192x192、512x512）
- **預估工時**：30 分鐘
- **效果**：Android/iOS 會顯示「加到主畫面」提示

#### 3.3 上傳提示 Toast 通知
- **為什麼**：學生點擊「上傳作品」開新分頁後，原頁面沒有回饋，可能困惑
- **怎麼做**：
  - 點擊後在頁面底部顯示浮動 Toast：「✅ 已開啟 Google Drive，請在新分頁中上傳」
  - 4 秒後自動淡出消失
  - CSS + JS 純前端實作，不需套件
- **預估工時**：15 分鐘

---

### 第二優先級（🟡 中）— 體驗提升

#### 3.4 班級密碼保護（簡易版）
- **為什麼**：增加一層防護，避免學生誤點其他班級
- **怎麼做**：
  - 點擊「上傳作品」時跳出密碼輸入 Modal
  - 每班可設不同密碼，存在 `config.js`
  - 使用 `sessionStorage` 記住已驗證狀態（同一瀏覽階段不重複驗證）
  - 密碼正確 → 導向 Google 登入 → Drive 資料夾
- **預估工時**：30 分鐘
- **注意**：前端密碼為「防君子不防小人」，真正的安全靠 Google Drive 帳號權限

#### 3.5 深色模式（Dark Mode）
- **怎麼做**：
  - 新增 `:root[data-theme="dark"]` CSS 變數組
  - 自動偵測 `prefers-color-scheme: dark`
  - Navbar 加入🌙/☀️ 切換按鈕
  - `localStorage` 記住使用者偏好
- **預估工時**：45 分鐘

#### 3.6 班級公告 / 最新消息
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

#### 3.7 QR Code 班級快捷
- **為什麼**：老師列印 QR Code 貼在教室，學生掃碼直達
- **怎麼做**：
  - 引入 `qrcode.js` 輕量套件（CDN）
  - 每張班級卡片加入「顯示 QR Code」按鈕
  - 彈窗顯示該班級的專屬 QR Code（連結為帶登入的完整 URL）
  - 支援下載 / 列印 QR Code
- **預估工時**：30 分鐘

#### 3.8 作品展示牆（Gallery）
- **為什麼**：展示優秀作品，增加學生成就感與學習動力
- **怎麼做**：
  - 新增 `#gallery` section
  - 使用 Google Drive API 讀取資料夾內圖片縮圖（需 API Key）
  - 瀑布流 / Masonry 排版
  - 燈箱效果點擊放大瀏覽
  - 可按班級篩選
- **預估工時**：2-3 小時（需申請 Google API Key）

---

### 第三優先級（🟢 低）— 進階功能

#### 3.9 倒數計時器
- **用途**：提醒學生上傳截止時間
- `config.js` 設定截止日期 → Hero 區或卡片顯示倒數（天:時:分:秒）
- 過期後按鈕變灰+顯示「已截止」
- **預估工時**：25 分鐘

#### 3.10 Google Sheets 上傳日誌
- **用途**：不需架設伺服器也能記錄使用統計
- Google Sheets + Apps Script 建立 Web API
- 每次點擊「上傳作品」時記錄（班級、時間、UA）
- 老師在 Sheets 查看各班使用頻率
- **預估工時**：45 分鐘

#### 3.11 Google Analytics 追蹤
- 加入 GA4 tracking code
- 自訂事件追蹤各班點擊次數
- GA 後台查看使用報表
- **預估工時**：10 分鐘

#### 3.12 自訂主題色彩
- `config.js` 加入 `THEME` 設定
- 支援多組主題：預設版、校慶版、聖誕版、母親節版
- 自動套用不同配色、裝飾元素
- **預估工時**：1 小時

#### 3.13 作品命名檢查器
- 跳轉 Drive 前顯示命名格式提醒彈窗
- 提供互動式命名產生器（選座號+輸入姓名+作品名稱 → 自動組合）
- 一鍵複製命名結果
- **預估工時**：30 分鐘

#### 3.14 LINE Notify 通知
- 串接 LINE Notify API
- 學生上傳後自動通知老師 LINE
- 需 serverless function（Cloudflare Workers / Vercel）
- **預估工時**：1-2 小時

#### 3.15 多語言支援（i18n）
- 建立 `js/i18n.js` 語言包（中文/英文）
- `data-i18n` 屬性標記可翻譯元素
- Navbar 加入語言切換按鈕
- **預估工時**：1 小時

---

## 四、技術改進建議 🔧

| 項目 | 說明 | 優先級 |
|------|------|--------|
| **OG Image PNG 化** | SVG 不被社群平台支援，需轉 PNG | 🔴 高 |
| **Favicon PNG 多尺寸** | 產生 16/32/180/192/512 px 的 PNG | 🟡 中 |
| **CSS 壓縮** | 使用 cssnano 或線上工具壓縮 CSS（預估可減少 30%） | 🟢 低 |
| **HTML 壓縮** | 使用 html-minifier 移除註解和空白 | 🟢 低 |
| **CDN 加速** | Cloudflare 免費方案加速 GitHub Pages | 🟢 低 |
| **自訂網域** | 購買域名（如 `craft.smes.tyc.edu.tw`）指向 GitHub Pages | 🟢 低 |
| **SEO 優化** | 加入 `sitemap.xml`、`robots.txt` | 🟢 低 |
| **Lighthouse 跑分** | 目標各項 90+，持續追蹤效能 | 🟡 中 |
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
├── index.html              # 主頁面 (v2.2, HTML5 語意化標籤)
├── css/
│   └── style.css           # 樣式表 (CSS Variables + RWD + 登入提示 + Footer 署名)
├── js/
│   ├── config.js           # 設定檔 (Drive ID + 學校信箱網域)
│   └── main.js             # 互動功能 (v2.2, 含登入導向機制)
├── images/
│   ├── favicon.svg         # 網站圖示 (三色漸層「作」字)
│   └── og-image.svg        # 社群分享預覽圖 (1200x630)
├── .gitignore
├── README.md               # 說明文件 (v2.2)
└── PROGRESS.md             # 本進度追蹤文件 (v2.2)
```

---

## 七、部署 Checklist

- [x] Google Drive 6 個班級資料夾 ID 已設定
- [x] 石門信箱登入導向機制已實作（`@mail2.smes.tyc.edu.tw`）
- [x] 聯絡 Email 已更新為 `ipad@mail2.smes.tyc.edu.tw`
- [x] Footer 已加入「Made with 💝 by 阿凱老師」+ 學校連結
- [x] 程式碼已推送至 GitHub（v2.2，共 6 個 commits）
- [x] README.md 含完整版本紀錄與登入機制說明
- [ ] 啟用 GitHub Pages（Settings → Pages → main branch）
- [ ] 確認 Google Drive 各資料夾權限（學校帳號可存取）
- [ ] 將 OG image 轉為 PNG 格式
- [ ] Lighthouse 效能檢測（目標 90+）
- [ ] LINE/FB 分享連結測試預覽卡片
- [ ] 手機實機測試 RWD + 登入導向流程

---

## 八、推薦實作順序 📋

如果你想逐步優化，建議按以下順序進行：

```
第 1 批（立即可做，10-15 分鐘）
  ├── ✅ 啟用 GitHub Pages
  ├── ✅ 確認 Drive 資料夾權限
  └── 📌 OG Image 轉 PNG

第 2 批（短期優化，30 分鐘內）
  ├── 📌 Toast 上傳提示通知
  ├── 📌 PWA 支援（加到主畫面）
  └── 📌 QR Code 班級快捷

第 3 批（中期功能，1-2 小時）
  ├── 📌 班級公告 / 最新消息
  ├── 📌 班級密碼保護
  ├── 📌 深色模式
  └── 📌 GA4 追蹤

第 4 批（進階功能，需更多時間）
  ├── 📌 作品展示牆 Gallery
  ├── 📌 Google Sheets 日誌
  ├── 📌 倒數計時器
  └── 📌 LINE Notify 通知
```
