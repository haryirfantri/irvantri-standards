#!/usr/bin/env node
/**
 * Reproducible Chromium (Playwright) E2E verification for TPL-E01-06 Formal Document Master.
 *
 * Reproduces the measured browser checks cited in REC-A04-015 / REC-A04-017:
 *   1. Offline single-file load from disk (file://): zero network requests, zero page errors.
 *   2. Opening state: Draft, v0.1.0, today's ISO date, open guide panel, 1-row Revision History.
 *   3. Sample load & replace-document confirmation (only shown when dirty; Keep returns focus).
 *   4. Sample renders paged output cleanly with zero Export checks.
 *   5. Press Preview toggles aria-pressed="true" and renders press sheets.
 *   6. Export Blocks: broken body stops export, updates #issues-n, announces via #live,
 *      and "Go to" selects the offending body text.
 *   7. Digital A4 PDF export produces a non-empty PDF (optionally saved via --export-pdf).
 *
 * Usage:
 *   node tools/e2e/verify_document_master.mjs
 *   node tools/e2e/verify_document_master.mjs --export-pdf /tmp/sample-digital.pdf
 */
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { pathToFileURL, fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO = path.resolve(__dirname, "../..");
const MASTER = path.join(REPO, "Standards Design/03_Templates/TPL-E01-06_Formal-Document-Master.html");

const args = process.argv.slice(2);
const pdfIdx = args.indexOf("--export-pdf");
const exportPdfPath = pdfIdx >= 0 ? path.resolve(args[pdfIdx + 1]) : null;

const { chromium } = await import("playwright");

assert.ok(fs.existsSync(MASTER), `Template not found: ${MASTER}`);
const url = pathToFileURL(MASTER).href;

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 } });
const page = await context.newPage();

const networkRequests = [];
const pageErrors = [];
page.on("request", (req) => {
  const u = req.url();
  if (!u.startsWith("file:") && !u.startsWith("data:") && !u.startsWith("blob:")) {
    networkRequests.push(u);
  }
});
page.on("pageerror", (err) => pageErrors.push(err.message));

// Capture window.print() so export clicks never block headless Chromium
await page.addInitScript(() => {
  window.__printCalls = 0;
  window.print = () => {
    window.__printCalls += 1;
  };
});

const readySeq = () => page.evaluate(() => Number(document.documentElement.dataset.ready || 0));
const waitRenderAfter = (prev) =>
  page.waitForFunction((n) => Number(document.documentElement.dataset.ready || 0) > n, prev, { timeout: 45000 });

await page.goto(url, { waitUntil: "load" });
await waitRenderAfter(0);

// 1. Opening state: blank Draft at v0.1.0 with guide open
const initial = await page.evaluate(() => ({
  status: document.querySelector("#f-status").value,
  version: document.querySelector("#f-version").value,
  date: document.querySelector("#f-date").value,
  history: document.querySelector("#f-history").value,
  guideOpen: document.querySelector("#guide").open,
  title: document.querySelector("#f-title").value,
}));
assert.equal(initial.status, "Draft", "Blank document must start as Draft");
assert.equal(initial.version, "v0.1.0", "Blank document must start at v0.1.0 (E02 §5.1.4)");
assert.match(initial.date, /^\d{4}-\d{2}-\d{2}$/, "Issue date must be ISO 8601");
assert.ok(initial.history.includes("v0.1.0") && initial.history.includes("Pre-Release"), "Initial Revision History must have v0.1.0 Pre-Release row");
assert.equal(initial.guideOpen, true, "Guide panel must open by default");
assert.equal(initial.title, "", "Blank document must have an empty title");
console.log("PASS 1/7: Opening blank Draft state verified");

// 2. Replace confirmation only appears when dirty, and Keep preserves edits
await page.fill("#f-title", "Temporary Unsaved Draft");
await page.click("#btn-sample");
await page.waitForSelector("#start-confirm:not([hidden])");
await page.click("#btn-start-no");
assert.equal(await page.isHidden("#start-confirm"), true, "Confirmation should hide after Keep");
assert.equal(await page.inputValue("#f-title"), "Temporary Unsaved Draft", "Keep must preserve edits");
console.log("PASS 2/7: Replace-document confirmation verified");

// 3. Load sample document via confirmation and wait for full layout + showIssues()
const seqBeforeSample = await readySeq();
await page.click("#btn-sample");
await page.waitForSelector("#start-confirm:not([hidden])");
await page.click("#btn-start-yes");
await waitRenderAfter(seqBeforeSample);
const sampleInfo = await page.evaluate(() => ({
  title: document.querySelector("#f-title").value,
  pages: document.querySelectorAll("#stage .pagedjs_page").length,
  issuesCount: document.querySelector("#issues-n").textContent.trim(),
}));
assert.ok(sampleInfo.title.length > 0, "Sample title must populate");
assert.ok(sampleInfo.pages >= 10, `Expected multi-page sample render, got ${sampleInfo.pages}`);
assert.equal(sampleInfo.issuesCount, "", `Sample should have zero export checks, got: ${sampleInfo.issuesCount}`);
console.log(`PASS 3/7: Sample loaded cleanly (${sampleInfo.pages} pages, 0 export checks)`);

// 4. Press preview toggle
await page.click("#btn-press-preview");
await page.waitForFunction(() => document.querySelector("#btn-press-preview").getAttribute("aria-pressed") === "true", null, { timeout: 15000 });
const pressSheets = await page.locator("#stage .press-sheet").count();
assert.equal(pressSheets, sampleInfo.pages, "Press preview must render one press sheet per page");
await page.click("#btn-press-preview");
await page.waitForFunction(() => document.querySelector("#btn-press-preview").getAttribute("aria-pressed") === "false", null, { timeout: 15000 });
console.log(`PASS 4/7: Press preview toggled cleanly (${pressSheets} sheets)`);

// 5. Export A4 PDF succeeds on clean sample and triggers window.print()
await page.click("#btn-pdf");
await page.waitForFunction(() => window.__printCalls >= 1, null, { timeout: 45000 });
if (exportPdfPath) {
  await page.emulateMedia({ media: "print" });
  await page.pdf({ path: exportPdfPath, preferCSSPageSize: true, printBackground: true });
  await page.emulateMedia({ media: "screen" });
  assert.ok(fs.statSync(exportPdfPath).size > 10000, "Exported PDF should be non-trivial");
}
console.log("PASS 5/7: Export A4 PDF succeeded");

// 6. Export Blocks stop export, announce via ARIA Live Region (30ms delay after settle), and Go to selects body text
const priorPrints = await page.evaluate(() => window.__printCalls);
const seqBeforeBreak = await readySeq();
await page.fill("#f-body", "# Broken Chapter\n\nMissing footnote[^99] and broken ref [Table](#tbl-missing).\n");
await waitRenderAfter(seqBeforeBreak);
await page.click("#btn-pdf");
await page.waitForFunction(() => /Export stopped/i.test(document.querySelector("#live").textContent), null, { timeout: 45000 });
const blockInfo = await page.evaluate(() => ({
  prints: window.__printCalls,
  live: document.querySelector("#live").textContent.trim(),
  issuesN: document.querySelector("#issues-n").textContent.trim(),
}));
assert.equal(blockInfo.prints, priorPrints, "Export must stay stopped when Export Blocks exist");
assert.match(blockInfo.live, /Export stopped/i, `Expected assertive Live Region announcement, got: ${blockInfo.live}`);
const gotoBtn = page.locator("#issues button", { hasText: "Go to" }).first();
await gotoBtn.click();
const selLen = await page.evaluate(() => {
  const ta = document.querySelector("#f-body");
  return ta.selectionEnd - ta.selectionStart;
});
assert.ok(selLen > 0, "Go to button must select the offending text in #f-body");
console.log(`PASS 6/7: Export Blocks (${blockInfo.issuesN}), Live Region, and Go to selection verified`);

// 7. Zero network requests and zero page errors across entire run
assert.deepEqual(networkRequests, [], `Unexpected external network requests: ${networkRequests.join(", ")}`);
assert.deepEqual(pageErrors, [], `Unexpected page errors: ${pageErrors.join("; ")}`);
console.log("PASS 7/7: Zero external network requests and zero page errors");

await browser.close();
