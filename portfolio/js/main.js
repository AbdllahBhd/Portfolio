"use strict";

/* Analytics: paste your GoatCounter code (the "xyz" in xyz.goatcounter.com) to switch it on.
   GoatCounter is privacy-friendly and cookie-free, so no consent banner is needed. */
const GOATCOUNTER_CODE = "";
if (GOATCOUNTER_CODE) {
  const gc = document.createElement("script");
  gc.async = true;
  gc.src = "https://gc.zgo.at/count.js";
  gc.dataset.goatcounter = `https://${GOATCOUNTER_CODE}.goatcounter.com/count`;
  document.head.appendChild(gc);
}
function track(name) { if (window.goatcounter && window.goatcounter.count) window.goatcounter.count({ path: "event/" + name, title: name, event: true }); }
document.querySelectorAll("[data-track]").forEach((el) => el.addEventListener("click", () => track(el.dataset.track)));

/* theme switch */
const root = document.documentElement;
const themeButtons = document.querySelectorAll("[data-set-theme]");
function setTheme(theme, save) {
  root.setAttribute("data-theme", theme);
  const meta = document.querySelector('meta[name="theme-color"]');
  if (meta) meta.content = getComputedStyle(root).getPropertyValue("--bg").trim();
  themeButtons.forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.setTheme === theme)));
  if (save) { try { localStorage.setItem("theme", theme); } catch (e) { /* storage blocked */ } track("theme-" + theme); }
}
setTheme(root.getAttribute("data-theme") || "light", false);
themeButtons.forEach((b) => b.addEventListener("click", () => setTheme(b.dataset.setTheme, true)));

/* progress bar, scroll-spy, back to top */
const bar = document.getElementById("progress"), toTop = document.getElementById("to-top");
// Only same-page anchors take part in scroll-spy; links to other pages are ignored.
const navLinks = [...document.querySelectorAll('.nav a[href^="#"], .case-nav a[href^="#"]')];
const sections = navLinks.map((a) => document.querySelector(a.getAttribute("href")));
function onScroll() {
  const max = document.documentElement.scrollHeight - innerHeight;
  bar.style.width = (max > 0 ? (scrollY / max) * 100 : 0) + "%";
  toTop.classList.toggle("show", scrollY > innerHeight);
  const y = scrollY + innerHeight * 0.35;
  let current = null;
  sections.forEach((s) => { if (s && y >= s.offsetTop) current = s; });
  navLinks.forEach((a, i) => sections[i] === current ? a.setAttribute("aria-current", "location") : a.removeAttribute("aria-current"));
}
onScroll(); addEventListener("scroll", onScroll, { passive: true }); addEventListener("resize", onScroll);
toTop.addEventListener("click", () => scrollTo({ top: 0 }));

/* copy buttons */
const toast = document.getElementById("toast");
function say(text) { toast.textContent = text; toast.classList.add("show"); clearTimeout(say.t); say.t = setTimeout(() => toast.classList.remove("show"), 1600); }
document.querySelectorAll("[data-copy]").forEach((b) => b.addEventListener("click", async () => {
  try { await navigator.clipboard.writeText(b.dataset.copy); say("Copied " + b.dataset.copy); track("copy"); } catch (e) { say("Copy not available: " + b.dataset.copy); }
}));

/* hover a technology: highlight the same tag everywhere (nothing is hidden) */
const tags = [...document.querySelectorAll(".tags li")];
const norm = (t) => t.trim().toLowerCase();
tags.forEach((tag) => {
  const on = () => tags.forEach((t) => t.classList.toggle("match", norm(t.textContent) === norm(tag.textContent)));
  const off = () => tags.forEach((t) => t.classList.remove("match"));
  tag.tabIndex = 0;
  tag.addEventListener("mouseenter", on); tag.addEventListener("mouseleave", off);
  tag.addEventListener("focus", on); tag.addEventListener("blur", off);
});

/* reveal + count-up */
const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
const io = new IntersectionObserver((entries) => entries.forEach((e) => {
  if (!e.isIntersecting) return;
  e.target.classList.add("in"); io.unobserve(e.target);
  e.target.querySelectorAll("[data-count]").forEach((el) => {
    if (reduce) return;
    const end = +el.dataset.count; let start = null;
    const step = (ts) => { start = start || ts; const p = Math.min(1, (ts - start) / 800); el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3))); if (p < 1) requestAnimationFrame(step); };
    requestAnimationFrame(step);
  });
}), { threshold: 0.08 });
document.querySelectorAll(".reveal").forEach((el) => io.observe(el));

/* work filters */
const filterButtons = [...document.querySelectorAll(".filters button")];
const workCards = [...document.querySelectorAll(".work .card")];
const filtersNote = document.querySelector(".filters-note");
filterButtons.forEach((button) => button.addEventListener("click", () => {
  const filter = button.dataset.filter;
  filterButtons.forEach((other) => other.setAttribute("aria-pressed", String(other === button)));
  let shown = 0;
  workCards.forEach((card) => {
    const match = filter === "all" || card.dataset.tags.split(" ").includes(filter);
    card.classList.toggle("is-hidden", !match);
    if (match) { shown += 1; card.classList.add("in"); }
  });
  filtersNote.textContent = filter === "all" ? "" : `Showing ${shown} of ${workCards.length} projects`;
  track("filter-" + filter);
}));

/* screenshot sliders */
document.querySelectorAll("[data-slider]").forEach((slider) => {
  const rail = slider.querySelector(".track");
  const slides = [...rail.children];
  const dots = slider.querySelector(".dots");
  const caption = slider.querySelector(".slide-caption");
  const prev = slider.querySelector(".prev"), next = slider.querySelector(".next");
  slides.forEach((_, i) => {
    const dot = document.createElement("button");
    dot.type = "button"; dot.setAttribute("aria-label", `Show screenshot ${i + 1} of ${slides.length}`);
    dot.addEventListener("click", () => go(i));
    dots.appendChild(dot);
  });
  const index = () => Math.round(rail.scrollLeft / rail.clientWidth);
  function go(i) { if (!rail.clientWidth) return; const target = Math.max(0, Math.min(slides.length - 1, i)); rail.scrollTo({ left: target * rail.clientWidth }); sync(target); }
  function sync(i = index()) {
    [...dots.children].forEach((d, k) => d.setAttribute("aria-current", String(k === i)));
    caption.textContent = `${i + 1}/${slides.length} · ${slides[i].querySelector("img").dataset.caption}`;
    prev.disabled = i === 0; next.disabled = i === slides.length - 1;
  }
  prev.addEventListener("click", () => { go(index() - 1); track("slide"); });
  next.addEventListener("click", () => { go(index() + 1); track("slide"); });
  rail.addEventListener("keydown", (e) => { if (e.key === "ArrowRight") { e.preventDefault(); go(index() + 1); } if (e.key === "ArrowLeft") { e.preventDefault(); go(index() - 1); } });
  let raf; rail.addEventListener("scroll", () => { cancelAnimationFrame(raf); raf = requestAnimationFrame(() => sync()); }, { passive: true });
  addEventListener("resize", () => { if (rail.clientWidth) go(index()); });
  sync(0);
});

/* lightbox */
const lightbox = document.getElementById("lightbox");
if (lightbox) {
// The image is created on first open: an <img> without src in the markup is invalid and reads as broken.
const lbImg = document.createElement("img"), lbCap = lightbox.querySelector("figcaption");
let lbSet = [], lbIndex = 0;
function showLb(i) { lbIndex = (i + lbSet.length) % lbSet.length; const img = lbSet[lbIndex]; lbImg.src = img.src; lbImg.alt = img.alt; if (!lbImg.isConnected) lbCap.before(lbImg); lbCap.textContent = img.alt + ` (${lbIndex + 1}/${lbSet.length})`; }
document.querySelectorAll("[data-zoom]").forEach((img) => (img.closest(".zoom") || img).addEventListener("click", () => {
  lbSet = [...img.closest("[data-slider]").querySelectorAll("img")]; showLb(lbSet.indexOf(img));
  if (typeof lightbox.showModal === "function") lightbox.showModal(); else window.open(img.src, "_blank");
  track("zoom");
}));
lightbox.querySelector(".close").addEventListener("click", () => lightbox.close());
lightbox.querySelector(".lb-prev").addEventListener("click", () => showLb(lbIndex - 1));
lightbox.querySelector(".lb-next").addEventListener("click", () => showLb(lbIndex + 1));
lightbox.addEventListener("click", (e) => { if (e.target === lightbox) lightbox.close(); });
lightbox.addEventListener("keydown", (e) => { if (e.key === "ArrowRight") showLb(lbIndex + 1); if (e.key === "ArrowLeft") showLb(lbIndex - 1); });

}

/* fit check */
const FIT = {
  dotnet: ["C# and ASP.NET Core daily in production since 2024", false],
  sql: ["Schema redesign and EF Core tuning, about 40% faster", false],
  front: ["Razor Pages in production; React for HEXIS", false],
  infra: ["Owns Linux, AWS, DNS, CI/CD and monitoring at MATMAK", false],
  pay: ["Stripe and Network International in production", false],
  lead: ["Led three client projects from requirements to launch", false],
  mobile: ["Flutter apps with Firebase, 2024 (secondary skill)", true],
  java: ["Eight months on Spring Boot microservices (secondary skill)", true],
};
const fitBox = document.getElementById("fit"), fitResult = document.getElementById("fit-result");
function renderFit() {
  const picked = [...fitBox.querySelectorAll("input:checked")].map((i) => i.value);
  if (!picked.length) { fitResult.textContent = "Tick what the role needs."; return; }
  const secondary = picked.filter((k) => FIT[k][1]).length;
  const verdict = secondary === 0 ? "Strong match" : secondary === picked.length ? "Partial match" : "Good match";
  fitResult.innerHTML = `<strong>${verdict}</strong> on ${picked.length} requirement${picked.length > 1 ? "s" : ""}:` +
    `<ul>${picked.map((k) => `<li class="${FIT[k][1] ? "sec" : ""}">${FIT[k][0]}</li>`).join("")}</ul>`;
}
if (fitBox && fitResult) {
  fitBox.addEventListener("change", () => { renderFit(); track("fit-check"); });
  renderFit();
}

/* footer year */
const currentYear = document.getElementById("current-year");
if (currentYear) currentYear.textContent = String(new Date().getFullYear());
