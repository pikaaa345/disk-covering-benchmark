"use strict";
// Protect TeX from Markdown escaping; copying uses the exact original source.
window.promptReady = (async () => {
  const source = document.getElementById("test-prompt").textContent.trim();
  const container = document.getElementById("prompt-markdown");
  const equations = [];
  const tokenPrefix = "DISKCOVERMATHPLACEHOLDER";
  if (source.includes(tokenPrefix)) throw new Error("Reserved math token in source");
  const displaySource = (container.dataset.article ? source.replace(/^#[^\n]*\n/, "") : source
    .replace(/^([^\n]+)\n/, (_, title) => "### " + title + "\n\n")
    .replace(/\*\*([^*\n]+)\*\*(?=[\p{L}\p{N}])/gu, (_, text) => "**" + text + "** "));
  const protectedSource = displaySource.replace(/\$\$[\s\S]*?\$\$|\$[^$\n]+?\$/g, equation => {
    const token = tokenPrefix + equations.length + "END";
    equations.push(equation);
    return token;
  });
  const escapeHtml = text => text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  if (container.dataset.format === "text") {
    container.innerHTML = '<pre class="document-text">' + escapeHtml(source) + '</pre>';
    container.dataset.rendered = "true";
    return true;
  }
  // Render only sanitized HTML, then typeset the protected TeX source.
  let rendered = marked.parse(protectedSource, {gfm: true, breaks: false});
  equations.forEach((equation, index) => {
    rendered = rendered.replace(tokenPrefix + index + "END", () => escapeHtml(equation));
  });
  container.innerHTML = DOMPurify.sanitize(rendered, {
    USE_PROFILES: {html: true},
    FORBID_TAGS: ["style", "form", "input", "button", "textarea", "select", "option"],
    FORBID_ATTR: ["style", "id", "name"],
    ALLOW_DATA_ATTR: false
  });
  await MathJax.startup.promise;
  await MathJax.typesetPromise([container]);
  container.dataset.rendered = "true";
  return true;
})();
window.promptReady.catch(error => {
  document.getElementById("copy-status").textContent = document.documentElement.lang === "en"
    ? "Formula rendering failed. You can still copy the source prompt."
    : "公式渲染失败，可复制原文";
  console.error(error);
});
