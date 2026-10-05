"use strict";
// Progressive enhancement: navigation links remain available without JavaScript.
document.addEventListener("DOMContentLoaded", () => {
  const header = document.querySelector(".site-header");
  const toggle = header?.querySelector(".site-menu-toggle");
  if (!header || !toggle) return;
  const mobile = window.matchMedia("(max-width: 1100px)");
  const setOpen = (open, restoreFocus = false) => {
    header.dataset.menuOpen = String(open);
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? toggle.dataset.closeLabel : toggle.dataset.openLabel);
    if (restoreFocus) toggle.focus();
  };
  toggle.hidden = false;
  document.documentElement.classList.add("navigation-ready");
  toggle.addEventListener("click", () => setOpen(toggle.getAttribute("aria-expanded") !== "true"));
  header.addEventListener("click", (event) => {
    if (event.target.closest("a[href]")) setOpen(false);
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && header.dataset.menuOpen === "true") setOpen(false, true);
  });
  document.addEventListener("click", (event) => {
    if (!header.contains(event.target)) setOpen(false);
  });
  mobile.addEventListener("change", () => setOpen(false));
});
