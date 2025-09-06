// Example: sidebar toggle (if you make it collapsible later)
// static/js/script.js
document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.querySelector(".sidebar-toggle");
    const sidebar = document.getElementById("sidebar");

    toggleBtn.addEventListener("click", () => {
        sidebar.classList.toggle("active");
    });
});


// script.js
function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    const mainContent = document.getElementById("main-content");
    sidebar.classList.toggle("collapsed");
}