function exponential_line() {
    var nav_items = document.getElementsByClassName("nav-item");

    for (var i = 0; i < nav_items.length; i++) {
        nav_items[i].classList.remove('active');
    }

    var short_line_nav = document.getElementById("exponential_line_nav")
    short_line_nav.classList.add("active");
}