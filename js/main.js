const menuBtn = document.querySelector(".menu-btn");
const navLinks = document.querySelector(".nav-links");

if (menuBtn && navLinks) {
  menuBtn.addEventListener("click", () => {
    const open = navLinks.classList.toggle("open");
    menuBtn.textContent = open ? "Close" : "Menu";
  });

  navLinks.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      navLinks.classList.remove("open");
      menuBtn.textContent = "Menu";
    });
  });
}

const filterBtns = document.querySelectorAll(".filter-btn");
const projectCards = document.querySelectorAll(".project-card");

if (filterBtns.length && projectCards.length) {
  filterBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      const filter = btn.dataset.filter || "all";

      filterBtns.forEach((b) => b.classList.remove("is-active"));
      btn.classList.add("is-active");

      projectCards.forEach((card) => {
        const categories = (card.dataset.categories || "").trim().split(/\s+/);
        const show = filter === "all" || categories.includes(filter);
        card.classList.toggle("is-hidden", !show);
      });
    });
  });
}
