/**
 * ============================================
 *  Google Drive 資料夾設定檔
 * ============================================
 *
 *  請將下方的 "YOUR_FOLDER_ID_HERE" 替換為
 *  各班級 Google Drive 資料夾的實際 ID。
 *
 *  如何取得資料夾 ID：
 *  1. 在 Google Drive 中建立六個班級資料夾
 *  2. 對每個資料夾點右鍵 → 「共用」→ 設定為「知道連結的人皆可編輯」
 *  3. 複製連結，格式如下：
 *     https://drive.google.com/drive/folders/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
 *                                          ↑ 這段就是資料夾 ID
 *  4. 將該 ID 貼到下方對應班級的欄位
 *
 *  權限建議：
 *  - 每個班級資料夾權限設定為僅限「特定使用者」（透過學校帳號）
 *  - 學生必須使用 @mail2.smes.tyc.edu.tw 帳號登入才能存取
 *  - 老師帳號保留「擁有者」權限，可管理所有資料夾
 *
 *  登入機制：
 *  - 點擊「上傳作品」時會先導向 Google 登入頁面
 *  - 自動預填學校信箱網域 @mail2.smes.tyc.edu.tw
 *  - 學生只需輸入帳號前半段（座號或姓名）即可快速登入
 *  - 登入成功後自動跳轉至對應班級的 Google Drive 資料夾
 */

const DRIVE_CONFIG = {
    // ============ Google Analytics 4 ============
    // 前往 https://analytics.google.com → 建立資源 → 取得 Measurement ID
    // 將下方 "G-XXXXXXXXXX" 替換為你的真實 GA4 ID
    // 留空或保持 "G-XXXXXXXXXX" 則不啟用追蹤
    GA4_MEASUREMENT_ID: "G-XXXXXXXXXX",

    // ============ 學校信箱網域設定 ============
    // 學生必須使用此網域的帳號登入 Google 才能存取資料夾
    // 格式：@xxx.xxx.xxx（含 @ 符號）
    SCHOOL_EMAIL_DOMAIN: "@mail2.smes.tyc.edu.tw",

    // ============ 班級 Google Drive 資料夾 ID ============

    // 六年一班
    CLASS_1_FOLDER_ID: "1ilQuNy_sIjHDWCwq7cCACA4P88NKGGAw",

    // 六年二班
    CLASS_2_FOLDER_ID: "1wOjG_r2ycrojOMfnniSU4bdAOuwk2aPA",

    // 六年三班
    CLASS_3_FOLDER_ID: "1yQw0frEPJwMQ6LMmGG70SmiGMo6BoQK9",

    // 六年四班
    CLASS_4_FOLDER_ID: "1sKJ3WCKSZ82YPiA99qSNstsCdC-scyVm",

    // 六年五班
    CLASS_5_FOLDER_ID: "1r09-M8zvBidI8KRRGrOrZ3-Ip0fJ9EHo",

    // 六年六班
    CLASS_6_FOLDER_ID: "1httfhfjrjq2IMCz2MG-CUZ0bMyzFpGTs",
};
