"use strict";

/* ------------------------------------------------------------------ theme */

const root = document.documentElement;
const themeToggle = document.querySelector(".theme-toggle");

function currentTheme() {
  const forced = root.getAttribute("data-theme");
  if (forced) return forced;
  return window.matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark";
}

if (themeToggle) {
  themeToggle.addEventListener("click", () => {
    const next = currentTheme() === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", next);
    try { localStorage.setItem("theme", next); } catch (error) { /* storage unavailable */ }
  });
}

/* ------------------------------------------------------------- mobile menu */

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
  menuButton.hidden = false;
  menuButton.addEventListener("click", () => setMenuState(menuButton.getAttribute("aria-expanded") !== "true"));
  primaryNav.addEventListener("click", (event) => {
    if (event.target.closest("a")) setMenuState(false);
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
}

/* --------------------------------------------------------------- scroll-spy */

const navLinks = [...document.querySelectorAll(".primary-nav a[href^='#'], .case-nav a[href^='#']")];
const spied = navLinks.map((link) => document.getElementById(link.getAttribute("href").slice(1))).filter(Boolean);

if (spied.length && "IntersectionObserver" in window) {
  const setCurrent = (id) => navLinks.forEach((link) => {
    if (link.getAttribute("href") === "#" + id) link.setAttribute("aria-current", "location");
    else link.removeAttribute("aria-current");
  });
  const spy = new IntersectionObserver((entries) => {
    const visible = entries.find((entry) => entry.isIntersecting);
    if (visible) setCurrent(visible.target.id);
  }, { rootMargin: "-35% 0px -60% 0px", threshold: 0 });
  spied.forEach((section) => spy.observe(section));
}

/* ------------------------------------------------------------ scroll reveal */

const revealTargets = [...document.querySelectorAll(".reveal")];
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

if (revealTargets.length && !reduceMotion && "IntersectionObserver" in window) {
  const revealer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add("in-view");
      revealer.unobserve(entry.target);
    });
  }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
  revealTargets.forEach((element) => revealer.observe(element));
} else {
  revealTargets.forEach((element) => element.classList.add("in-view"));
}

/* ------------------------------------------------------------------ footer */

const currentYear = document.querySelector("#current-year");
if (currentYear) currentYear.textContent = String(new Date().getFullYear());
