# 手作課作品上傳平台

讓學生透過網頁直接上傳手作課照片與影片至 Google Drive 班級資料夾。

## 快速開始

### 1. 建立 Google Drive 資料夾

在你的 Google Drive 中建立以下資料夾結構：

```
手作課作品/
├── 六年一班/
├── 六年二班/
├── 六年三班/
├── 六年四班/
├── 六年五班/
└── 六年六班/
```

### 2. 設定資料夾權限

對每個班級資料夾：

1. 右鍵點擊資料夾 → **共用**
2. 在「一般存取權」設定為 **「知道連結的人皆可編輯」**
3. 複製共用連結

> 連結格式：`https://drive.google.com/drive/folders/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
>
> 其中 `XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX` 就是資料夾 ID

### 3. 設定網站連結

打開 `js/config.js`，將各班級的 `YOUR_FOLDER_ID_HERE` 替換為實際的資料夾 ID：

```js
const DRIVE_CONFIG = {
    CLASS_1_FOLDER_ID: "1aBcDeFgHiJkLmNoPqRsTuVwXyZ",  // 六年一班
    CLASS_2_FOLDER_ID: "2aBcDeFgHiJkLmNoPqRsTuVwXyZ",  // 六年二班
    // ...以此類推
};
```

### 4. 部署到 GitHub Pages

```bash
# 初始化 git 並推送
git init
git add .
git commit -m "初始化手作課上傳平台"
git branch -M main
git remote add origin https://github.com/你的帳號/你的repo名稱.git
git push -u origin main
```

然後到 GitHub：
1. 進入 Repository → **Settings** → **Pages**
2. Source 選擇 **Deploy from a branch**
3. Branch 選擇 **main**，資料夾選擇 **/ (root)**
4. 點擊 **Save**

網站會部署在：`https://你的帳號.github.io/你的repo名稱/`

## 權限管理建議

| 角色 | 權限等級 | 說明 |
|------|---------|------|
| 老師 | 擁有者 | 可管理所有資料夾內容 |
| 該班學生 | 編輯者 | 透過連結可上傳檔案 |
| 其他班學生 | 無權限 | 不知道其他班的資料夾連結 |

- 每個班級只能透過網站上的按鈕看到自己班級的資料夾連結
- 如需更嚴格的權限控制，可改為透過 Google 群組設定特定帳號的存取權

## 檔案結構

```
├── index.html          # 主頁面
├── css/
│   └── style.css       # 樣式表
├── js/
│   ├── config.js       # Google Drive 資料夾 ID 設定
│   └── main.js         # 網站互動功能
└── README.md           # 本說明文件
```
