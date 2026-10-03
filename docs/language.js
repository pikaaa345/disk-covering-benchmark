"use strict";
// One preference for every page. English is the default, regardless of OS locale.
(() => {
  const root = document.documentElement;
  const current = root.lang === "en" ? "en" : "zh";
  const requested = new URL(location.href).searchParams.get("lang");
  let saved;
  try { saved = localStorage.getItem("diskcover-language"); } catch (_) {}
  const language = ["en", "zh"].includes(requested) ? requested
    : ["en", "zh"].includes(saved) ? saved : "en";
  try { localStorage.setItem("diskcover-language", language); } catch (_) {}
  window.siteLanguage = language;
  // Preserve links to the former combined report while opening a single test.
  if (root.dataset.page === "records" && ["#astra", "#sol"].includes(location.hash)) {
    const model = location.hash.slice(1);
    const destination = new URL("record-n11-" + model + "-20260930" + (language === "zh" ? ".zh" : "") + ".html", location.href);
    destination.search = location.search;
    destination.searchParams.set("lang", language);
    location.replace(destination.href);
    return;
  }
  if (language !== current) {
    const destination = new URL(root.dataset.page + (language === "zh" ? ".zh" : "") + ".html", location.href);
    destination.search = location.search;
    destination.hash = location.hash;
    location.replace(destination.href);
    return;
  }
  // Query parameters keep navigation consistent even if storage is disabled.
  document.addEventListener("DOMContentLoaded", () => {
    const updateLinks = () => {
      for (const link of document.querySelectorAll("a[href]")) {
        const destination = new URL(link.getAttribute("href"), location.href);
        if (destination.origin !== location.origin || !destination.pathname.endsWith(".html")) continue;
        destination.searchParams.set("lang", link.dataset.language || language);
        link.href = destination.href;
      }
    };
    updateLinks();
    new MutationObserver(updateLinks).observe(document.body, {childList:true, subtree:true});
  });
})();
