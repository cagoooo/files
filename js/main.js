/**
 * 手作課作品上傳平台 - 主程式
 */

// ========== Google Drive 資料夾開啟 ==========
function openDriveFolder(element, event) {
    event.preventDefault();
    const folderKey = element.getAttribute("data-folder");
    const folderId = DRIVE_CONFIG[folderKey];

    if (!folderId || folderId === "YOUR_FOLDER_ID_HERE") {
        document.getElementById("configModal").style.display = "flex";
        return;
    }

    window.open(
        `https://drive.google.com/drive/folders/${folderId}`,
        "_blank"
    );
}

function closeModal() {
    document.getElementById("configModal").style.display = "none";
}

// 點擊 overlay 關閉 modal
document.addEventListener("click", function (e) {
    if (e.target.classList.contains("modal-overlay")) {
        closeModal();
    }
});

// ========== Navbar 行動版選單 ==========
document.querySelector(".nav-toggle").addEventListener("click", function () {
    document.querySelector(".nav-links").classList.toggle("active");
});

// 點擊導覽連結後關閉選單
document.querySelectorAll(".nav-links a").forEach(function (link) {
    link.addEventListener("click", function () {
        document.querySelector(".nav-links").classList.remove("active");
    });
});

// ========== Navbar 捲動效果 ==========
window.addEventListener("scroll", function () {
    var navbar = document.querySelector(".navbar");
    if (window.scrollY > 20) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }
});

// ========== 捲動進場動畫 ==========
function handleScrollAnimations() {
    var elements = document.querySelectorAll(
        ".class-card, .step-card, .tips-box"
    );
    elements.forEach(function (el) {
        var rect = el.getBoundingClientRect();
        if (rect.top < window.innerHeight - 80) {
            el.classList.add("visible");
        }
    });
}

window.addEventListener("scroll", handleScrollAnimations);
window.addEventListener("load", handleScrollAnimations);
