"use strict";
const PAGE_CONFIG = Object.freeze(JSON.parse(document.getElementById("page-config").textContent));
const messages = PAGE_CONFIG.language === "en" ? {
  copied: "Copied", selected: "Full prompt selected. Please copy it manually.",
  invalid: "Enter a 64-character hexadecimal SHA256 using only 0–9 and a–f.",
  pending: "Valid format. The reference hash is not published yet, so a match cannot be determined.",
  matched: "Fingerprint matches.", mismatch: "Fingerprint does not match. Check your answer and the protocol."
} : {
  copied: "已复制", selected: "已选中全文，请手动复制",
  invalid: "请输入 64 位十六进制 SHA256，仅包含 0–9 与 a–f。",
  pending: "格式正确。标准哈希待发布，暂时无法判断答案是否匹配。",
  matched: "指纹匹配。", mismatch: "指纹不匹配，请检查答案与协议。"
};
const button = document.getElementById("copy-prompt");
button.addEventListener("click", async () => {
  const target = document.getElementById("test-prompt");
  const status = document.getElementById("copy-status");
  const text = target.textContent.trim();
  let copied = false;
  if (navigator.clipboard && window.isSecureContext) {
    try { await navigator.clipboard.writeText(text); copied = true; } catch (_) {}
  }
  if (!copied) {
    const helper = document.createElement("textarea");
    helper.value = text;
    helper.style.position = "fixed";
    helper.style.left = "-9999px";
    document.body.appendChild(helper);
    helper.select();
    try { copied = document.execCommand("copy"); } finally { helper.remove(); button.focus(); }
  }
  if (copied) {
    status.textContent = messages.copied;
  } else {
    target.hidden = false;
    const range = document.createRange();
    range.selectNodeContents(target);
    const selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
    status.textContent = messages.selected;
  }
});
const reference = PAGE_CONFIG.referenceSha256;
if(reference) document.getElementById("reference-hash").textContent = reference;
const hashForm = document.getElementById("hash-form");
if (hashForm) hashForm.addEventListener("submit", event => {
  event.preventDefault();
  const digest = document.getElementById("hash-input").value.trim().toLowerCase();
  const result = document.getElementById("hash-result");
  result.className = "note";
  if(!/^[0-9a-f]{64}$/.test(digest)) {
    result.classList.add("error");
    result.textContent = messages.invalid;
  } else if(!reference) {
    result.textContent = messages.pending;
  } else if(digest === reference.toLowerCase()) {
    result.classList.add("match");
    result.textContent = messages.matched;
  } else {
    result.classList.add("error");
    result.textContent = messages.mismatch;
  }
});
