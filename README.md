# 手作課作品上傳平台 v3.0

> 讓學生透過網頁直接上傳手作課照片與影片至 Google Drive 班級資料夾。
>
> 🔗 **線上版**：[https://cagoooo.github.io/files/](https://cagoooo.github.io/files/)

---

## 功能特色

- 🏫 **6 個班級專區**（601～606），各自對應獨立 Google Drive 資料夾
- 🔐 **石門信箱登入**：點擊上傳按鈕後自動導向 Google 登入頁，預填 `@mail2.smes.tyc.edu.tw` 網域
- 🎨 **繽紛 UI**：Fredoka + Nunito 字體、6 色漸層卡片、shimmer/glow 動效
- 📱 **RWD 響應式**：桌面 3 欄 / 平板 2 欄 / 手機 1 欄
- ♿ **無障礙設計**：ARIA 標籤、focus-visible、ESC 關閉、reduced-motion
- 🔗 **社群分享**：完整 OG / Twitter / LINE meta tags

---

## 快速開始

### 1. 設定 Google Drive 資料夾權限

對每個班級資料夾：
1. 右鍵點擊資料夾 → **共用**
2. 新增學生帳號（`@mail2.smes.tyc.edu.tw`）為**編輯者**
3. 或設定為「知道連結的人皆可編輯」

### 2. 設定資料夾 ID（已完成）

`js/config.js` 已設定好 6 個班級的 Google Drive 資料夾 ID：

```js
const DRIVE_CONFIG = {
    SCHOOL_EMAIL_DOMAIN: "@mail2.smes.tyc.edu.tw",  // 學校信箱網域

    CLASS_1_FOLDER_ID: "1ilQuNy_sIjHDWCwq7cCACA4P88NKGGAw",  // 601
    CLASS_2_FOLDER_ID: "1wOjG_r2ycrojOMfnniSU4bdAOuwk2aPA",  // 602
    CLASS_3_FOLDER_ID: "1yQw0frEPJwMQ6LMmGG70SmiGMo6BoQK9",  // 603
    CLASS_4_FOLDER_ID: "1sKJ3WCKSZ82YPiA99qSNstsCdC-scyVm",  // 604
    CLASS_5_FOLDER_ID: "1r09-M8zvBidI8KRRGrOrZ3-Ip0fJ9EHo",  // 605
    CLASS_6_FOLDER_ID: "1httfhfjrjq2IMCz2MG-CUZ0bMyzFpGTs",  // 606
};
```

### 3. 部署到 GitHub Pages

已推送至 GitHub。啟用 Pages：

1. 進入 Repository → **Settings** → **Pages**
2. Source 選擇 **Deploy from a branch**
3. Branch 選擇 **main**，資料夾選擇 **/ (root)**
4. 點擊 **Save**

網站會部署在：`https://cagoooo.github.io/files/`

---

## 學生使用流程

```
① 選擇班級 → ② 點擊「上傳作品」→ ③ 自動跳轉 Google 登入頁
                                      （帳號欄已預填 @mail2.smes.tyc.edu.tw）
                                   → ④ 輸入帳號前半段 → 登入
                                   → ⑤ 自動進入 Drive 資料夾 → 上傳檔案
```

---

## 登入機制說明

點擊班級的「上傳作品」按鈕後，系統會組合以下 Google 登入 URL：

```
https://accounts.google.com/v3/signin/identifier
  ?Email=@mail2.smes.tyc.edu.tw           ← 預填學校信箱網域
  &continue=https://drive.google.com/drive/folders/{FOLDER_ID}  ← 登入後跳轉
  &flowName=GlifWebSignIn
  &flowEntry=AddSession
```

- 學生在登入頁只需輸入帳號的**前半段**（如座號或姓名拼音）
- 網域 `@mail2.smes.tyc.edu.tw` 已自動帶入
- 登入成功後自動跳轉至對應班級的 Google Drive 資料夾

---

## 權限管理建議

| 角色 | 權限等級 | 說明 |
|------|---------|------|
| 老師 | 擁有者 | 可管理所有資料夾內容 |
| 該班學生 | 編輯者 | 透過石門信箱帳號登入後可上傳 |
| 其他人 | 無權限 | 未授權帳號無法存取 |

---

## 檔案結構

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
├── README.md               # 本說明文件
└── PROGRESS.md             # 開發進度與未來優化規劃
```

---

## 版本紀錄

| 版本 | 日期 | 說明 |
|------|------|------|
| v3.0 | 2026-03-18 | Toast 上傳提示、PWA 支援（加到主畫面）、QR Code 班級快捷（產生/下載/列印）|
| v2.2 | 2026-03-18 | 更新聯絡 Email、Footer 加入阿凱老師署名與學校連結、版本號統一更新 |
| v2.1 | 2026-03-18 | 加入石門信箱登入導向機制、預填學校信箱網域 |
| v2.0 | 2026-03-18 | 全面 UI/UX 優化、Fredoka + Nunito 字體、載入動畫、IntersectionObserver |
| v1.0 | 2026-03-18 | 初始版本：6 班級 Google Drive 串接、RWD、基礎 UI |
