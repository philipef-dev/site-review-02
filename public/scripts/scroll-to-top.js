(function () {
  function initScrollToTop() {
    const scrollUp = document.getElementById("scroll-up");
    if (!scrollUp) return;

    function toggleScrollUp() {
      if (window.scrollY > 300) {
        scrollUp.classList.remove("opacity-0", "pointer-events-none");
        scrollUp.classList.add("opacity-100");
      } else {
        scrollUp.classList.add("opacity-0", "pointer-events-none");
        scrollUp.classList.remove("opacity-100");
      }
    }

    function scrollToTop() {
      window.scrollTo({ top: 0, behavior: "smooth" });
    }

    scrollUp.addEventListener("click", scrollToTop);
    scrollUp.addEventListener("keydown", function (event) {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        scrollToTop();
      }
    });

    window.addEventListener("scroll", toggleScrollUp, { passive: true });
    toggleScrollUp();
  }

  window.addEventListener("load", initScrollToTop);
})();
