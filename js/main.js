"use strict";

const menuButton = document.querySelector(".menu-btn");
const primaryNav = document.querySelector(".primary-nav");
const mobileQuery = window.matchMedia("(max-width: 760px)");

function setMenuState(isOpen) {
  if (!menuButton || !primaryNav) return;
  primaryNav.classList.toggle("is-open", isOpen);
  menuButton.setAttribute("aria-expanded", String(isOpen));
  menuButton.textContent = isOpen ? "Close" : "Menu";
}

if (menuButton && primaryNav) {
  menuButton.addEventListener("click", () => setMenuState(menuButton.getAttribute("aria-expanded") !== "true"));
  primaryNav.addEventListener("click", (event) => {
    const link = event.target.closest("a");
    if (!link) return;
    setMenuState(false);
    const href = link.getAttribute("href");
    if (mobileQuery.matches && href?.startsWith("#")) {
      const target = document.getElementById(href.slice(1));
      if (target) window.setTimeout(() => {
        target.setAttribute("tabindex", "-1");
        target.focus({ preventScroll: true });
        target.addEventListener("blur", () => target.removeAttribute("tabindex"), { once: true });
      }, 0);
    }
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && menuButton.getAttribute("aria-expanded") === "true") {
      setMenuState(false);
      menuButton.focus();
    }
  });
  document.addEventListener("click", (event) => {
    if (!primaryNav.contains(event.target) && !menuButton.contains(event.target)) setMenuState(false);
  });
  mobileQuery.addEventListener("change", () => setMenuState(false));
  menuButton.hidden = false;
  document.documentElement.classList.add("nav-enhanced");
}

const currentYear = document.querySelector("#current-year");
if (currentYear) currentYear.textContent = String(new Date().getFullYear());
