"use strict";
window.MathJax = {
  loader: {
    load: ["ui/safe"],
    source: {"ui/safe": "[mathjax]/mathjax-ui-safe.js"}
  },
  tex: {
    inlineMath: [["$", "$"], ["\\(", "\\)"]],
    displayMath: [["$$", "$$"], ["\\[", "\\]"]],
    processEscapes: true
  },
  svg: {fontCache: "local"},
  options: {
    enableMenu: false,
    safeOptions: {
      allow: {URLs: "safe", classes: "safe", cssIDs: "safe", styles: "none"},
      safeProtocols: {https: true, http: false, file: false, javascript: false, data: false}
    }
  },
  startup: {typeset: false}
};
