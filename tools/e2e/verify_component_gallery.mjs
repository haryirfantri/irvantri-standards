#!/usr/bin/env node
/**
 * Reproducible Chromium (Playwright) E2E + Reflow + Accessibility verification
 * for AST-D03-02 Component Gallery + AST-D03-01 Component Kit + AST-D01-02 Tokens.
 *
 * Verifies:
 *   1. Offline load from disk (file://): zero network requests, zero page/console errors.
 *   2. Responsive reflow at 320 px (Compact, D02 §5.1.1), 768 px (Medium), and 1280 px (Expanded):
 *      zero horizontal overflow, and `.is-table--reflow` switches to stacked cards below 768 px (D03 §5.3.3).
 *   3. Keyboard focus & visible 3 px Brand Blue focus indicator (D04 §5.2.3–5.2.4).
 *   4. Confirmation <dialog id="confirm"> opens via #open-dialog and closes via #cancel.
 *   5. axe-core WCAG 2.2 AA accessibility audit (zero violations).
 *
 * Usage:
 *   node tools/e2e/verify_component_gallery.mjs
 */
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { pathToFileURL, fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO = path.resolve(__dirname, "../..");
const GALLERY = path.join(REPO, "Standards Design/02_Assets/AST-D03-02_Component-Gallery.html");

const { chromium } = await import("playwright");

assert.ok(fs.existsSync(GALLERY), `Component Gallery not found: ${GALLERY}`);
const url = pathToFileURL(GALLERY).href;

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1280, height: 900 } });
const page = await context.newPage();

const networkRequests = [];
const pageErrors = [];
const consoleErrors = [];
page.on("request", (req) => {
  const u = req.url();
  if (!u.startsWith("file:") && !u.startsWith("data:") && !u.startsWith("blob:")) {
    networkRequests.push(u);
  }
});
page.on("pageerror", (err) => pageErrors.push(err.message));
page.on("console", (msg) => {
  if (msg.type() === "error") consoleErrors.push(msg.text());
});

await page.goto(url, { waitUntil: "load" });

// 1. Stylesheets loaded and custom properties applied
const tokenCheck = await page.evaluate(() => {
  const cs = getComputedStyle(document.documentElement);
  return {
    brandPrimary: cs.getPropertyValue("--is-color-brand-primary").trim(),
    focusWidth: cs.getPropertyValue("--is-focus-ring-width").trim(),
    bodyBg: getComputedStyle(document.body).backgroundColor,
  };
});
assert.equal(tokenCheck.brandPrimary.toUpperCase(), "#074C96", "AST-D01-02 tokens must load");
assert.equal(tokenCheck.focusWidth, "3px", "Focus ring width must be 3px (D04 §5.2.3)");
console.log("PASS 1/5: Tokens and component kit stylesheets loaded cleanly");

// 2. Reflow check across 320 px (Compact), 768 px (Medium), and 1280 px (Expanded)
for (const width of [320, 768, 1280]) {
  await page.setViewportSize({ width, height: 900 });
  const layout = await page.evaluate(() => {
    const thead = document.querySelector(".is-table--reflow thead");
    const firstRow = document.querySelector(".is-table--reflow tbody tr");
    return {
      innerWidth: window.innerWidth,
      scrollWidth: document.documentElement.scrollWidth,
      theadDisplay: thead ? getComputedStyle(thead).display : "",
      rowDisplay: firstRow ? getComputedStyle(firstRow).display : "",
    };
  });
  assert.ok(
    layout.scrollWidth <= layout.innerWidth + 1,
    `Horizontal overflow at ${width}px: scrollWidth=${layout.scrollWidth} > innerWidth=${layout.innerWidth}`,
  );
  if (width < 768) {
    assert.equal(layout.theadDisplay, "none", "Reflow table must hide thead below 768px (D03 §5.3.3)");
    assert.equal(layout.rowDisplay, "block", "Reflow table rows must render as stacked cards below 768px");
  } else {
    assert.notEqual(layout.theadDisplay, "none", `Table thead should be visible at ${width}px`);
  }
}
console.log("PASS 2/5: Responsive reflow verified at 320 px, 768 px, and 1280 px (0 overflow)");

// 3. Keyboard focus & visible 3 px Brand Blue focus outline (D04 §5.2.3–5.2.4)
await page.setViewportSize({ width: 1280, height: 900 });
await page.keyboard.press("Tab"); // Skip link
await page.keyboard.press("Tab"); // First primary button ("Save changes")
const focusInfo = await page.evaluate(() => {
  const el = document.activeElement;
  const cs = getComputedStyle(el);
  return {
    tag: el.tagName,
    text: el.textContent.trim(),
    outlineStyle: cs.outlineStyle,
    outlineWidth: cs.outlineWidth,
    outlineColor: cs.outlineColor,
  };
});
assert.equal(focusInfo.tag, "BUTTON", `Expected focus on button, got ${focusInfo.tag}`);
assert.equal(focusInfo.outlineStyle, "solid", "Focus outline must be solid");
assert.equal(focusInfo.outlineWidth, "3px", "Focus outline must be 3px (D04 §5.2.3)");
assert.equal(focusInfo.outlineColor, "rgb(7, 76, 150)", "Focus outline must be Brand Blue #074C96 (D04 §5.2.4)");
console.log(`PASS 3/5: Keyboard focus indicator verified (${focusInfo.outlineWidth} ${focusInfo.outlineStyle} ${focusInfo.outlineColor})`);

// 4. Confirmation dialog opens and closes cleanly
await page.click("#open-dialog");
assert.equal(await page.evaluate(() => document.getElementById("confirm").open), true, "Dialog must open");
await page.click("#cancel");
assert.equal(await page.evaluate(() => document.getElementById("confirm").open), false, "Dialog must close on cancel");
console.log("PASS 4/5: Confirmation dialog interaction verified");

// 5. axe-core WCAG 2.2 AA accessibility audit + zero errors/network requests
const axeMod = await import("axe-core");
const axeSource = axeMod.default?.source || axeMod.source;
assert.ok(axeSource, "axe-core source must load");
await page.addScriptTag({ content: axeSource });
const axeResults = await page.evaluate(async () => {
  return await window.axe.run(document, {
    runOnly: { type: "tag", values: ["wcag2a", "wcag2aa", "wcag21aa", "wcag22aa"] },
  });
});
if (axeResults.violations.length > 0) {
  const summary = axeResults.violations.map((v) => `${v.id} (${v.impact}): ${v.help} [${v.nodes.length} node(s)]`).join("\n  ");
  assert.fail(`axe-core reported ${axeResults.violations.length} WCAG 2.2 AA violation(s):\n  ${summary}`);
}
assert.deepEqual(networkRequests, [], `Unexpected external network requests: ${networkRequests.join(", ")}`);
assert.deepEqual(pageErrors, [], `Unexpected page errors: ${pageErrors.join("; ")}`);
assert.deepEqual(consoleErrors, [], `Unexpected console errors: ${consoleErrors.join("; ")}`);
console.log(`PASS 5/5: axe-core WCAG 2.2 AA passed (${axeResults.passes.length} rules passed, 0 violations, 0 network/console errors)`);

await browser.close();
