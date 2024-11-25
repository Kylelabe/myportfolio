// Toggle menu animation
document.addEventListener("DOMContentLoaded", function () {
  const toggleButton = document.getElementById("menu-toggle");

  toggleButton.addEventListener("click", function () {
    toggleButton.classList.toggle("toggled");

    // Toggle both collapse elements
    const collapses = document.querySelectorAll(
      "#bs-example-navbar-collapse-1, #bs-example-navbar-collapse-2"
    );
    collapses.forEach((collapse) => {
      collapse.classList.toggle("in"); // Simulates the Bootstrap "in" class for showing the menu
    });
  });
});

// Smooth scroll for anchor links
document.querySelectorAll('.navbar-scroll-to a[href^="#"]').forEach((link) => {
  link.addEventListener("click", function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute("href"));
    if (target) {
      window.scrollTo({
        top: target.offsetTop - 50, // Adjust based on navbar height
        behavior: "smooth",
      });
    }
  });
});
