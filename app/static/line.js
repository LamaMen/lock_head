var current_page;

if (window.location.href == "https://blackbirdteam.pythonanywhere.com/tasks") { current_page = document.getElementById('a1'); }
else if (window.location.href == "https://blackbirdteam.pythonanywhere.com/") { current_page = document.getElementById('a2'); }
else { current_page = document.getElementById('a3'); }

current_page.style.borderBottom = "2px solid #F8E015";

var menu_links = document.getElementById('menu').getElementsByTagName('a');

for (var i = 0; i < menu_links.length; i++) {
    menu_links[i].onmouseover = function () {
        this.style.borderBottom = "2px solid #F8E015";
        if (this != current_page) {
            current_page.style.borderBottom = "2px solid transparent";
        }
    }
    menu_links[i].onmouseout = function () {
        if (this != current_page)
            this.style.borderBottom = "2px solid transparent";
        if (this != current_page) {
            current_page.style.borderBottom = "2px solid #F8E015";
        }
    }
}