/* TPL-E01-06 Formal Document Master: application logic.
   Governing: E01 (v2.6.0) §5.5 HTML Authoring Master Profile; E05 (v1.0.0) Document Body Elements.
   Source: tools/document-master/app.js, inlined by tools/build_document_master.py. */
(function () {
  'use strict';

  // The untouched master, captured before anything changes, is the base of every Filled Copy (E01 §5.5.6).
  const PRISTINE = '<!DOCTYPE html>\n' + document.documentElement.outerHTML;
  const STORE_KEY = 'tpl-e01-06-autosave';

  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const MM = 96 / 25.4;
  const TEXT_W_MM = 170;

  const FIELDS = ['f-title', 'f-subtitle', 'f-category', 'f-identifier', 'f-version', 'f-status', 'f-date', 'f-owner', 'f-approver',
    'f-superseded', 'f-waiver', 'f-waiver-expiry', 'f-body', 'f-distribution', 'f-history'];
  const OPTIONS = ['o-twosided', 'o-watermark', 'o-section', 'o-lot', 'o-lof', 'o-back'];
  const LABELS = {
    'f-title': 'Document title', 'f-subtitle': 'Subtitle', 'f-category': 'Category', 'f-identifier': 'Identifier', 'f-version': 'Version',
    'f-status': 'Status', 'f-date': 'Issue date', 'f-owner': 'Owner', 'f-approver': 'Approver', 'f-superseded': 'Superseded by',
    'f-waiver': 'Waiver ID', 'f-waiver-expiry': 'Waiver expiry', 'f-body': 'Body', 'f-distribution': 'Distribution list', 'f-history': 'Revision history'
  };
  const STATUS_ROLE = { 'Planned': 'informative', 'In Review': 'informative', 'Draft': 'warning', 'Approved': 'success', 'Sync Required': 'warning', 'Deprecated': 'danger' };

  let images = {};          // name -> { type, data (data URI), w, h, svg (text, SVG only) }
  let dirty = false;
  const touched = new Set();
  let lastIssues = [];
  let pressView = false;

  // ------------------------------------------------------------------ state
  function collect() {
    const fields = {}, options = {};
    FIELDS.forEach(id => { fields[id] = $(id).value; });
    OPTIONS.forEach(id => { options[id] = $(id).checked; });
    return { v: 1, fields, options, images };
  }
  function apply(state) {
    if (!state || !state.fields) return;
    FIELDS.forEach(id => { if (state.fields[id] != null) $(id).value = state.fields[id]; });
    OPTIONS.forEach(id => { if (state.options && state.options[id] != null) $(id).checked = !!state.options[id]; });
    images = state.images || {};
    renderImageList();
  }
  function sampleState() {
    const svg = $('sample-diagram').textContent.trim();
    return {
      v: 1,
      fields: {
        'f-title': 'Document Master Element Reference', 'f-subtitle': 'How every body element looks in a formal document',
        'f-category': 'Reference', 'f-identifier': 'REF-001', 'f-version': 'v1.0.0', 'f-status': 'Approved', 'f-date': '2026-11-28',
        'f-owner': 'Hary Irfantri', 'f-approver': 'Hary Irfantri', 'f-superseded': '', 'f-waiver': '', 'f-waiver-expiry': '',
        'f-body': $('sample-body').textContent.trim(), 'f-distribution': 'Hary Irfantri | Owner and Approver | Irvantri Standards Pte. Ltd.',
        'f-history': $('sample-history').textContent.trim()
      },
      options: { 'o-twosided': false, 'o-watermark': false, 'o-section': true, 'o-lot': true, 'o-lof': true, 'o-back': true },
      images: { 'authoring-flow.svg': { type: 'image/svg+xml', data: 'data:image/svg+xml;base64,' + btoa(unescape(encodeURIComponent(svg))), svg, w: 640, h: 220 } }
    };
  }

  // ------------------------------------------------------------------ field rules (E01 §5.1.3, §5.5.4; E02)
  const ISO = /^\d{4}-\d{2}-\d{2}$/;
  function validDate(s) {
    if (!ISO.test(s)) return false;
    const d = new Date(s + 'T00:00:00Z');
    return !isNaN(d) && d.toISOString().slice(0, 10) === s;
  }
  function fieldErrors() {
    const f = collect().fields, e = {};
    const need = (id, fix) => { if (!f[id].trim()) e[id] = `${LABELS[id]} is empty. ${fix}`; };
    need('f-title', 'Enter the document title.');
    need('f-identifier', 'Enter the document identifier.');
    need('f-owner', 'Enter the Owner\'s full name.');
    need('f-approver', 'Enter the Approver\'s full name.');
    if (!/^v\d+\.\d+\.\d+$/.test(f['f-version'].trim())) e['f-version'] = 'Version must read vMAJOR.MINOR.ERRATA, such as v1.0.0 (A01 §5.5.1).';
    else if (f['f-status'] === 'Approved' && /^v0\./.test(f['f-version'].trim())) e['f-version'] = 'An Approved document needs v1.0.0 or later; v0.Y.0 is for drafts (E02 §5.1.4).';
    if (!validDate(f['f-date'].trim())) e['f-date'] = 'Issue date must be a real date written YYYY-MM-DD (C04 §5.1.1).';
    if (f['f-status'] === 'Deprecated' && !f['f-superseded'].trim()) e['f-superseded'] = 'A Deprecated document must name the document that replaces it (E02 §5.4.2).';
    if (f['f-status'] !== 'Deprecated' && f['f-superseded'].trim()) e['f-superseded'] = 'Superseded by applies only to Deprecated documents. Clear it or set the status to Deprecated.';
    const w = f['f-waiver'].trim(), we = f['f-waiver-expiry'].trim();
    if (w && !/^REC-A04-\d{3}$/.test(w)) e['f-waiver'] = 'Waiver ID must read REC-A04-000 (E02 §5.3.5).';
    if (w && !validDate(we)) e['f-waiver-expiry'] = 'Enter the waiver expiry as YYYY-MM-DD (E02 §5.3.5).';
    if (!w && we) e['f-waiver'] = 'Enter the Waiver ID that this expiry belongs to, or clear the expiry.';
    if (!f['f-body'].trim()) e['f-body'] = 'The body is empty. Write or paste the document content.';
    f['f-distribution'].split('\n').map(s => s.trim()).filter(Boolean).forEach((line, i) => {
      const parts = line.split('|').map(s => s.trim());
      if (parts.length !== 3 || parts.some(p => !p)) e['f-distribution'] = `Line ${i + 1} needs three parts: Name | Role | Organization.`;
    });
    if (!/\|\s*Version\s*\|\s*Date\s*\|\s*Type\s*\|\s*Summary of Changes\s*\|\s*Approver\s*\|/i.test(f['f-history'])) {
      e['f-history'] = 'Revision history must be a table with the columns Version, Date, Type, Summary of Changes and Approver (E02 §5.1.3).';
    } else {
      const rows = f['f-history'].split('\n').filter(l => /^\s*\|/.test(l)).slice(2);
      const first = rows[0] && rows[0].split('|')[1];
      if (!rows.length) e['f-history'] = 'Revision history has no rows. Add the current version first.';
      else if (first && first.trim().replace(/`/g, '') !== f['f-version'].trim()) e['f-history'] = `The newest revision history row is ${first.trim()}, but the version is ${f['f-version'].trim() || 'empty'}. Put the current version first (E02 §5.1.3).`;
    }
    if (f['f-status'] === 'Approved' && $('o-watermark').checked) e['f-status'] = 'Approved documents cannot carry the review watermark (E02 §5.3.4). Turn off Review watermark in Options.';
    return e;
  }
  function showFieldErrors(all) {
    const e = fieldErrors();
    FIELDS.forEach(id => {
      const out = $(id.replace('f-', 'e-'));
      const show = (all || touched.has(id)) && e[id];
      if (out) out.textContent = show ? e[id] : '';
      $(id).setAttribute('aria-invalid', show ? 'true' : 'false');
    });
    return e;
  }

  // ------------------------------------------------------------------ Markdown (E05 §5.1)
  const md = new marked.Marked({ gfm: true, breaks: false });
  let ctx = null; // per-render context: footnote definitions, issues
  md.use({
    extensions: [
      { name: 'fnref', level: 'inline', start: s => s.indexOf('[^'),
        tokenizer(src) { const m = /^\[\^([^\]\s]+)\]/.exec(src); if (m) return { type: 'fnref', raw: m[0], id: m[1] }; },
        renderer(t) {
          const def = ctx.footnotes[t.id];
          if (def == null) { ctx.issues.push({ msg: `Footnote [^${t.id}] has no text. Add a line "[^${t.id}]: text" (E05 §5.7.1).`, field: 'f-body' }); return '<sup>?</sup>'; }
          ctx.usedFootnotes.add(t.id);
          return `<span class="fn">${md.parseInline(def)}</span>`;
        } },
      { name: 'kbd', level: 'inline', start: s => s.indexOf('[['),
        tokenizer(src) { const m = /^\[\[([^\]\n]{1,30})\]\]/.exec(src); if (m) return { type: 'kbd', raw: m[0], text: m[1] }; },
        renderer(t) { return `<kbd>${esc(t.text)}</kbd>`; } },
      { name: 'sup', level: 'inline', start: s => s.indexOf('^'),
        tokenizer(src) { const m = /^\^([^\^\s](?:[^\^\n]{0,40}[^\^\s])?)\^/.exec(src); if (m) return { type: 'sup', raw: m[0], text: m[1] }; },
        renderer(t) { return `<sup>${esc(t.text)}</sup>`; } },
      { name: 'sub', level: 'inline', start: s => { const i = s.search(/(^|[^~])~(?!~)/); return i < 0 ? -1 : (s[i] === '~' ? i : i + 1); },
        tokenizer(src) { const m = /^~(?!~)([^~\s](?:[^~\n]{0,40}[^~\s])?)~(?!~)/.exec(src); if (m) return { type: 'sub', raw: m[0], text: m[1] }; },
        renderer(t) { return `<sub>${esc(t.text)}</sub>`; } },
      { name: 'deflist', level: 'block', start: s => { const m = /\n[^\n]+\n: /.exec('\n' + s); return m ? m.index : -1; },
        tokenizer(src) {
          const re = /^([^\n:][^\n]*)\n((?:: [^\n]*(?:\n|$))+)\n*/;
          let rest = src, raw = '', items = [], m;
          while ((m = re.exec(rest))) {
            if (/^\s*([-*+]|\d+\.|#|>|\|)/.test(m[1])) break;
            items.push({ term: m[1].trim(), defs: m[2].split('\n').filter(Boolean).map(l => l.replace(/^: /, '')) });
            raw += m[0]; rest = rest.slice(m[0].length);
          }
          if (items.length) return { type: 'deflist', raw, items };
        },
        renderer(t) {
          return '<dl class="deflist">' + t.items.map(i => `<dt>${md.parseInline(i.term)}</dt>` + i.defs.map(d => `<dd>${md.parseInline(d)}</dd>`).join('')).join('') + '</dl>';
        } }
    ],
    renderer: {
      // Raw HTML is shown as text, never rendered (E05 §5.1.3).
      html(t) { return esc(t.text || t.raw || ''); },
      checkbox(t) { return `<span class="box${t.checked ? ' on' : ''}" role="img" aria-label="${t.checked ? 'Done' : 'Not done'}"></span>`; },
      image(t) { return `<img data-src="${esc(t.href)}" alt="${esc(t.text || '')}" data-title="${esc(t.title || '')}">`; },
      link(t) {
        const text = this.parser.parseInline(t.tokens);
        if (!text.trim() && /^#/.test(t.href)) return `<a class="xref" href="${esc(t.href)}" data-mode="${t.title === 'page' ? 'page' : 'label'}"></a>`;
        if (/^javascript:/i.test(t.href)) return text;
        return `<a href="${esc(t.href)}">${text}</a>`;
      },
      code(t) {
        const info = (t.lang || '').trim();
        const lang = (info.match(/^[^\s{]*/) || [''])[0];
        if (lang === 'signoff') return signoffHtml(t.text);
        const lines = /\{lines\}/.test(info);
        const body = lines ? t.text.split('\n').map((l, i) => `<span class="l"><span class="n" aria-hidden="true">${i + 1}</span>${esc(l) || ' '}</span>`).join('') : esc(t.text);
        return `<pre${lines ? ' class="ln"' : ''}>${lang ? `<span class="lang" aria-hidden="true">${esc(lang)}</span>` : ''}<code>${body}</code></pre>`;
      }
    }
  });

  function signoffHtml(text) {
    const blocks = text.split(/\n\s*\n/).map(b => {
      const o = {};
      b.split('\n').forEach(l => { const m = /^\s*(Name|Role|Date)\s*:\s*(.*)$/i.exec(l); if (m) o[m[1].toLowerCase()] = m[2].trim(); });
      return o;
    }).filter(o => Object.keys(o).length);
    blocks.forEach((o, i) => {
      if (!o.name || !o.role) ctx.issues.push({ msg: `Sign-off block, signatory ${i + 1}: Name and Role are required (E05 §5.5.7).`, field: 'f-body' });
      if (o.date && !validDate(o.date)) ctx.issues.push({ msg: `Sign-off block, signatory ${i + 1}: write the date as YYYY-MM-DD (C04 §5.1.1).`, field: 'f-body' });
    });
    return '<div class="signoff">' + blocks.map(o => `<div class="sig"><dl><dt>Name</dt><dd>${esc(o.name || '')}</dd><dt>Role</dt><dd>${esc(o.role || '')}</dd><dt>Date</dt><dd>${esc(o.date || '—')}</dd></dl><div class="line">Signature</div></div>`).join('') + '</div>';
  }

  // ------------------------------------------------------------------ images
  function svgColorsOk(svg) {
    const allowed = new Set(Object.values(palette()).map(v => v.toUpperCase()));
    const bad = new Set();
    (svg.match(/#[0-9A-Fa-f]{6}\b|#[0-9A-Fa-f]{3}\b/g) || []).forEach(h => {
      const full = h.length === 4 ? '#' + h.slice(1).split('').map(c => c + c).join('') : h;
      if (!allowed.has(full.toUpperCase())) bad.add(h);
    });
    (svg.match(/rgba?\([^)]*\)/g) || []).forEach(c => bad.add(c));
    return [...bad];
  }
  let paletteCache = null;
  function palette() {
    if (paletteCache) return paletteCache;
    const cs = getComputedStyle(document.documentElement), out = {};
    ['brand-primary', 'brand-accent', 'brand-deep', 'brand-secondary', 'bg-surface', 'bg-canvas', 'bg-muted', 'bg-tint', 'border-subtle', 'border-default',
      'text-muted', 'text-primary', 'text-mono'].concat(['informative', 'success', 'warning', 'danger', 'neutral'].flatMap(r => [`status-${r}`, `status-${r}-bg`, `status-${r}-border`]))
      .forEach(k => { out[k] = cs.getPropertyValue('--is-color-' + k).trim(); });
    return (paletteCache = out);
  }
  function sanitizeSvg(text, prefix) {
    const doc = new DOMParser().parseFromString(text, 'image/svg+xml');
    const svg = doc.documentElement;
    if (!svg || svg.nodeName.toLowerCase() !== 'svg' || doc.querySelector('parsererror')) return null;
    svg.querySelectorAll('script, foreignObject, iframe, image, use[href^="http"], style').forEach(n => n.remove());
    svg.querySelectorAll('*').forEach(el => {
      [...el.attributes].forEach(a => {
        if (/^on/i.test(a.name)) el.removeAttribute(a.name);
        if ((a.name === 'href' || a.name === 'xlink:href') && !/^#/.test(a.value)) el.removeAttribute(a.name);
      });
      if (el.id) el.id = prefix + el.id;
      ['href', 'xlink:href'].forEach(n => { const v = el.getAttribute(n); if (v && v[0] === '#') el.setAttribute(n, '#' + prefix + v.slice(1)); });
      ['fill', 'stroke', 'marker-end', 'marker-start', 'clip-path', 'mask', 'filter'].forEach(n => {
        const v = el.getAttribute(n); if (v && /url\(#/.test(v)) el.setAttribute(n, v.replace(/url\(#/g, 'url(#' + prefix));
      });
    });
    svg.removeAttribute('width'); svg.removeAttribute('height');
    return svg.outerHTML;
  }
  function addImageFile(file) {
    return new Promise((resolve) => {
      const reader = new FileReader();
      reader.onload = () => {
        const data = reader.result;
        let base = (file.name || 'image').replace(/[^\w.-]+/g, '-');
        if (!/\.(svg|png|jpe?g)$/i.test(base)) base += file.type === 'image/svg+xml' ? '.svg' : file.type === 'image/png' ? '.png' : '.jpg';
        let name = base, n = 2;
        while (images[name]) name = base.replace(/(\.\w+)$/, `-${n++}$1`);
        const entry = { type: file.type, data };
        const done = () => { images[name] = entry; renderImageList(); markDirty(); resolve(name); };
        if (file.type === 'image/svg+xml') {
          const svg = decodeURIComponent(escape(atob(data.split(',')[1])));
          entry.svg = svg;
          const vb = /viewBox\s*=\s*["']\s*[-\d.]+[\s,]+[-\d.]+[\s,]+([\d.]+)[\s,]+([\d.]+)/.exec(svg);
          entry.w = vb ? +vb[1] : 600; entry.h = vb ? +vb[2] : 400;
          done();
        } else {
          const img = new Image();
          img.onload = () => { entry.w = img.naturalWidth; entry.h = img.naturalHeight; done(); };
          img.onerror = () => { announce(`${file.name} could not be read as an image.`); resolve(null); };
          img.src = data;
        }
      };
      reader.readAsDataURL(file);
    });
  }
  function renderImageList() {
    const ul = $('image-list');
    ul.innerHTML = '';
    Object.keys(images).forEach(name => {
      const li = document.createElement('li');
      const im = images[name];
      li.innerHTML = `<code>${esc(name)}</code><span>${im.w || '?'} × ${im.h || '?'}</span>`;
      const b = document.createElement('button');
      b.type = 'button'; b.className = 'btn'; b.textContent = 'Remove'; b.setAttribute('aria-label', `Remove image ${name}`);
      b.addEventListener('click', () => { delete images[name]; renderImageList(); markDirty(); schedule(); });
      li.appendChild(b);
      ul.appendChild(li);
    });
    if (!ul.children.length) ul.innerHTML = '<li><span>No images yet.</span></li>';
  }

  // ------------------------------------------------------------------ build the document
  function parseBlock(mdText) {
    const tpl = document.createElement('template');
    tpl.innerHTML = '<div>' + md.parse(mdText) + '</div>';
    return tpl.content.firstChild;
  }
  function takeAttrs(text) {
    const out = { text, id: null, landscape: false };
    out.text = out.text.replace(/\s*\{#([\w-]+)\}/g, (_, id) => { out.id = id; return ''; });
    out.text = out.text.replace(/\s*\{landscape\}/g, () => { out.landscape = true; return ''; });
    out.text = out.text.trim();
    return out;
  }

  function buildDocument(fillers) {
    const s = collect(), f = s.fields, o = s.options;
    const issues = [];
    ctx = { issues, footnotes: {}, usedFootnotes: new Set() };
    const st = f['f-status'], role = STATUS_ROLE[st];
    const stVars = `--st-fg: var(--is-color-status-${role}); --st-bg: var(--is-color-status-${role}-bg); --st-border: var(--is-color-status-${role}-border);`;
    const year = (f['f-date'] || '').slice(0, 4);
    const ver = esc(f['f-version'].trim());
    const bannerText = st === 'Approved' ? '' : `${esc(st)} — ${ver} | Non-Binding Working Copy. Do not distribute as an Approved baseline.`;
    const lockup = $('lockup-svg').textContent.trim();

    // Footnote definitions (single line): [^id]: text
    let body = f['f-body'].replace(/\r\n?/g, '\n').replace(/^\[\^([^\]\s]+)\]:[ \t]+(.+)$/gm, (_, id, text) => { ctx.footnotes[id] = text; return ''; });
    body = body.replace(/^\\pagebreak[ \t]*$/gm, '\n@@PAGEBREAK@@\n');
    const box = parseBlock(body);
    box.querySelectorAll('p').forEach(p => { if (p.textContent.trim() === '@@PAGEBREAK@@') { const d = document.createElement('div'); d.className = 'startpage pb'; p.replaceWith(d); } });
    Object.keys(ctx.footnotes).forEach(id => { if (!ctx.usedFootnotes.has(id)) issues.push({ msg: `Footnote [^${id}] is defined but never used. Remove it or cite it (E05 §5.7.1).`, field: 'f-body' }); });

    // Parts and heading numbers (E05 §5.2.3, §5.8)
    const RANK = { body: 0, appendix: 1, glossary: 2, references: 3 };
    let part = 'body', lastRank = 0, n = [0, 0, 0], appLetter = 0, firstH1Seen = false;
    const toc = [], targets = {};
    const seenBack = { glossary: 0, references: 0 };
    let idx = 0;
    box.querySelectorAll('h1, h2, h3, h4').forEach(h => {
      const lvl = +h.tagName[1];
      const a = takeAttrs(h.innerHTML);
      h.innerHTML = a.text;
      const plain = h.textContent.trim();
      if (lvl === 1) {
        firstH1Seen = true;
        const m = /^Appendix\s+([A-Z])\s*[—–-]\s*(.+)$/.exec(plain);
        if (m) part = 'appendix';
        else if (/^Glossary$/i.test(plain)) part = 'glossary';
        else if (/^References$/i.test(plain)) part = 'references';
        else part = 'body';
        if (RANK[part] < lastRank) issues.push({ msg: `"${plain}" is out of order. Parts run: body, appendices, glossary, references (E05 §5.8.1).`, field: 'f-body' });
        lastRank = Math.max(lastRank, RANK[part]);
        if (part === 'glossary' || part === 'references') { if (++seenBack[part] > 1) issues.push({ msg: `There is more than one ${part} section (E05 §5.8.1).`, field: 'f-body' }); }
        if (part === 'appendix') {
          appLetter++;
          const letter = String.fromCharCode(64 + appLetter);
          if (m[1] !== letter) issues.push({ msg: `"${plain}" should be Appendix ${letter}: appendices are lettered in order (E05 §5.8.3).`, field: 'f-body' });
          n = [appLetter, 0, 0];
        } else if (part === 'body') { n[0]++; n[1] = 0; n[2] = 0; }
        h.classList.add('part-' + part);
        h.dataset.start = '1';
      } else if (lvl <= 3 && (part === 'body' || part === 'appendix')) {
        n[lvl - 1]++; for (let k = lvl; k < 3; k++) n[k] = 0;
      }
      let num = '', label = '';
      if (part === 'body' && lvl <= 3) { num = n.slice(0, lvl).join('.'); label = 'Section ' + num; }
      if (part === 'appendix' && lvl <= 3) {
        const L = String.fromCharCode(64 + n[0]);
        num = lvl === 1 ? '' : [L].concat(n.slice(1, lvl)).join('.');
        label = lvl === 1 ? 'Appendix ' + L : 'Section ' + num;
      }
      if (part === 'glossary' && lvl === 1) label = 'Glossary';
      if (part === 'references' && lvl === 1) label = 'References';
      if (num) { h.innerHTML = `<span class="hn">${num}</span> ` + h.innerHTML; }
      h.id = a.id || ('h-' + (++idx));
      if (a.id) { if (targets[a.id]) issues.push({ msg: `The id {#${a.id}} is used twice (E05 §5.7.2).`, field: 'f-body' }); targets[a.id] = label || plain; }
      h.dataset.part = part;
      if (lvl === 1 || (lvl === 2 && (part === 'body' || part === 'appendix'))) toc.push({ lvl, num: num || (part === 'appendix' && lvl === 1 ? '' : ''), id: h.id, text: lvl === 1 && part === 'appendix' ? plain : h.textContent.replace(num, '').trim() });
      if (lvl === 1 && o['o-section']) h.dataset.secname = plain;
    });
    if (!firstH1Seen && f['f-body'].trim()) issues.push({ msg: 'The body has no level-1 heading. Start each chapter with "# Title" (E05 §5.2.2).', field: 'f-body' });

    // Callouts, summary, notes, quotations (E05 §5.5)
    let summaries = 0;
    box.querySelectorAll('blockquote').forEach(bq => {
      const p = bq.querySelector('p');
      const m = p && /^\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION|SUMMARY)\]\s*/.exec(p.innerHTML);
      if (m) {
        const kind = m[1].toLowerCase();
        p.innerHTML = p.innerHTML.slice(m[0].length).replace(/^<br>\s*/, '');
        const div = document.createElement('aside');
        if (kind === 'summary') {
          summaries++;
          div.className = 'summary';
          div.innerHTML = '<span class="ct">Summary</span>' + bq.innerHTML;
          if (bq.closest('div') !== box || [...box.children].indexOf(bq) > [...box.children].findIndex(e => e.tagName === 'H1') && box.querySelector('h1'))
            issues.push({ msg: 'The summary box must come before the first chapter heading (E05 §5.8.1).', field: 'f-body' });
        } else {
          div.className = 'callout ' + kind;
          div.innerHTML = `<span class="ct">${kind[0].toUpperCase() + kind.slice(1)}</span>` + bq.innerHTML;
        }
        bq.replaceWith(div);
        return;
      }
      const first = p && p.firstElementChild;
      if (first && first.tagName === 'STRONG' && /^(Informative Note|Example):$/.test(first.textContent) && p.innerHTML.indexOf('<strong>') === 0) {
        const div = document.createElement('aside');
        div.className = 'note-block';
        const label = first.textContent.replace(/:$/, '');
        first.remove();
        p.innerHTML = p.innerHTML.replace(/^\s+/, '');
        div.innerHTML = `<span class="ct">${label}</span>` + bq.innerHTML;
        bq.replaceWith(div);
        return;
      }
      const last = bq.lastElementChild;
      if (last && /^\s*—\s/.test(last.textContent)) last.classList.add('attrib');
    });
    if (summaries > 1) issues.push({ msg: `There are ${summaries} summary boxes. A document has at most one (E05 §5.5.4).`, field: 'f-body' });

    // Requirement clauses (E05 §5.5.6)
    box.querySelectorAll('p').forEach(p => {
      const s0 = p.firstChild;
      if (s0 && s0.nodeType === 1 && s0.tagName === 'STRONG' && /^\d+(\.\d+)+$/.test(s0.textContent.trim())) {
        p.classList.add('clause');
        const span = document.createElement('span'); span.className = 'cn'; span.textContent = s0.textContent.trim();
        s0.replaceWith(span);
        if (span.nextSibling && span.nextSibling.nodeType === 3) span.nextSibling.textContent = span.nextSibling.textContent.replace(/^\s+/, '');
      }
    });

    // Lists (E05 §5.3)
    box.querySelectorAll('li').forEach(li => {
      if (li.firstElementChild && li.firstElementChild.classList.contains('box')) li.classList.add('task');
      const pb = li.querySelector(':scope > p > .box'); if (pb) li.classList.add('task');
    });
    if (box.querySelector('li li li li')) issues.push({ msg: 'A list nests four levels deep. Lists stop at three levels (E05 §5.3.1).', field: 'f-body' });

    // References list (E05 §5.7.3)
    box.querySelectorAll('h1.part-references').forEach(h => { let el = h.nextElementSibling; while (el && el.tagName !== 'H1') { if (el.tagName === 'OL') el.classList.add('refs'); el = el.nextElementSibling; } });

    // Numbering scope for tables and figures: body N, appendix A1 (E05 §5.8.3)
    const scopeOf = (el) => {
      let p = el; while (p && p.parentElement !== box) p = p.parentElement;
      let prev = p; while (prev && !(prev.tagName === 'H1')) prev = prev.previousElementSibling;
      if (prev && prev.dataset.part === 'appendix') { const m = /Appendix\s+([A-Z])/.exec(prev.textContent); return m ? 'app:' + m[1] : ''; }
      return '';
    };
    const counters = {};
    const nextLabel = (kind, el) => {
      const sc = scopeOf(el);
      const L = sc.startsWith('app:') ? sc.slice(4) : '';
      const key = kind + (L || '');
      counters[key] = (counters[key] || 0) + 1;
      return `${kind} ${L}${counters[key]}`;
    };
    const tables = [], figures = [];
    const distRows = f['f-distribution'].split('\n').map(l => l.trim()).filter(Boolean).map(l => l.split('|').map(x => x.trim()));
    if (distRows.length) { counters['Table'] = 1; tables.push({ label: 'Table 1', text: 'Distribution list', id: 'tbl-distribution' }); }

    // Tables (E05 §5.4)
    box.querySelectorAll('table').forEach(t => {
      const prev = t.previousElementSibling;
      let cap = null;
      if (prev && prev.tagName === 'P' && /^Table:\s*/.test(prev.textContent)) { cap = takeAttrs(prev.innerHTML.replace(/^Table:\s*/, '')); prev.remove(); }
      const label = nextLabel('Table', t);
      if (!cap || !cap.text) issues.push({ msg: `${label} has no caption. Add a line "Table: caption" just above it (E05 §5.4.1).`, field: 'f-body' });
      const c = document.createElement('caption');
      c.innerHTML = `<b>${label}.</b> ${cap ? cap.text : ''}`;
      t.prepend(c);
      t.id = (cap && cap.id) || ('t-' + tables.length);
      if (cap && cap.id) { if (targets[cap.id]) issues.push({ msg: `The id {#${cap.id}} is used twice (E05 §5.7.2).`, field: 'f-body' }); targets[cap.id] = label; }
      tables.push({ label, text: cap ? cap.text.replace(/<[^>]+>/g, '') : '', id: t.id });
      t.querySelectorAll('[align="right"]').forEach(x => { x.classList.add('num'); });
      t.querySelectorAll('[align="center"]').forEach(x => { x.classList.add('ctr'); });
      t.querySelectorAll('[align]').forEach(x => x.removeAttribute('align'));
      t.querySelectorAll('tbody tr').forEach((tr, r) => {
        [...tr.children].forEach((td, ci) => {
          if (!td.textContent.trim() && !td.querySelector('img, svg')) {
            const col = (t.querySelectorAll('thead th')[ci] || {}).textContent || `column ${ci + 1}`;
            issues.push({ msg: `${label}, row ${r + 1}, ${col}: the cell is blank. Enter None or — (C04 §5.4.1).`, field: 'f-body' });
          }
        });
      });
      const rows = t.querySelectorAll('tbody tr');
      const lastRow = rows[rows.length - 1];
      if (lastRow && /^Total/i.test(lastRow.firstElementChild.textContent.trim())) lastRow.classList.add('total');
      const next = t.nextElementSibling;
      if (next && next.tagName === 'P' && /^(Source|Note):/.test(next.textContent.trim())) { next.className = 'tsource'; t.classList.add('has-source'); }
      if (cap && cap.landscape) {
        const wrap = document.createElement('div'); wrap.className = 'land';
        const rot = document.createElement('div'); rot.className = 'rot';
        t.replaceWith(wrap); rot.appendChild(t);
        if (next && next.classList.contains('tsource')) rot.appendChild(next);
        wrap.appendChild(rot);
      }
    });

    // Figures (E05 §5.6)
    let figN = 0;
    box.querySelectorAll('p').forEach(p => {
      const imgs = [...p.querySelectorAll('img')];
      if (!imgs.length) return;
      const onlyImgs = [...p.childNodes].every(nd => (nd.nodeType === 1 && (nd.tagName === 'IMG' || nd.tagName === 'BR')) || (nd.nodeType === 3 && !nd.textContent.trim()));
      if (!onlyImgs) {
        issues.push({ msg: 'An image sits inside a paragraph of text. Put each figure on its own line (E05 §5.6.3).', field: 'f-body' });
        imgs.forEach(i => i.remove());
        return;
      }
      if (imgs.length > 2) issues.push({ msg: 'A figure holds more than two images. Use at most two side by side (E05 §5.6.3).', field: 'f-body' });
      const label = nextLabel('Figure', p); figN++;
      let capText = null, capId = null;
      const nx = p.nextElementSibling;
      if (nx && nx.tagName === 'P' && /^Figure:\s*/.test(nx.textContent)) { const a = takeAttrs(nx.innerHTML.replace(/^Figure:\s*/, '')); capText = a.text; capId = a.id; nx.remove(); }
      if (imgs.length === 1 && capText == null) { const a = takeAttrs(esc(imgs[0].dataset.title || '')); capText = a.text; capId = a.id; }
      const fig = document.createElement('figure');
      const wrap = document.createElement('div'); wrap.className = 'imgs';
      imgs.slice(0, 2).forEach((img, k) => {
        const cell = document.createElement('div');
        const src = img.dataset.src || '';
        const alt = img.getAttribute('alt') || '';
        if (!alt.trim()) issues.push({ msg: `${label} has no alternative text. Describe the image inside ![...] (E05 §5.6.1).`, field: 'f-body' });
        const maxMm = imgs.length > 1 ? (TEXT_W_MM - 8) / 2 : TEXT_W_MM;
        let entry = images[src] || null;
        if (!entry && /^data:image\//.test(src)) entry = { type: src.slice(5, src.indexOf(';')), data: src };
        if (!entry) {
          issues.push({ msg: /^https?:/i.test(src) ? `${label} links to ${src}. Masters work offline: download the image and add it with Add image (E01 §5.5.8).`
            : `${label} uses "${src}", which is not in Images. Add it with Add image (E05 §5.6.2).`, field: 'f-body' });
          cell.innerHTML = `<div class="sub">[Missing image: ${esc(src)}]</div>`;
        } else if (entry.type === 'image/svg+xml') {
          const svgText = entry.svg || decodeURIComponent(escape(atob(entry.data.split(',')[1])));
          const bad = svgColorsOk(svgText);
          if (bad.length) issues.push({ msg: `${label} (${src}) uses colors outside B02: ${bad.slice(0, 4).join(', ')}. Redraw it with palette colors (E05 §5.6.4).`, field: 'f-body' });
          const clean = sanitizeSvg(svgText, `f${figN}${k}-`);
          const wmm = Math.min(maxMm, (entry.w || 600) / MM);
          cell.innerHTML = clean ? clean.replace(/^<svg/, `<svg role="img" aria-label="${esc(alt)}" style="width: ${wmm.toFixed(1)}mm; height: auto; display: block; margin: 0 auto"`) : '';
          if (!clean) issues.push({ msg: `${label} (${src}) is not a readable SVG file.`, field: 'f-body' });
        } else {
          const wmm = Math.min(maxMm, ((entry.w || 600) / 300) * 25.4);
          cell.innerHTML = `<img src="${entry.data}" alt="${esc(alt)}" style="width: ${wmm.toFixed(1)}mm" data-raster="1">`;
        }
        if (imgs.length > 1) cell.insertAdjacentHTML('beforeend', `<div class="sub">(${'ab'[k]}) ${img.dataset.title ? esc(takeAttrs(img.dataset.title).text) : esc(alt)}</div>`);
        wrap.appendChild(cell);
      });
      fig.appendChild(wrap);
      const fc = document.createElement('figcaption');
      fc.innerHTML = `<b>${label}.</b> ${capText || ''}`;
      if (!capText) issues.push({ msg: `${label} has no caption. Add a title in quotes after the file name, or a "Figure: caption" line below (E05 §5.6.1).`, field: 'f-body' });
      fig.appendChild(fc);
      fig.id = capId || ('fig-' + figN);
      if (capId) { if (targets[capId]) issues.push({ msg: `The id {#${capId}} is used twice (E05 §5.7.2).`, field: 'f-body' }); targets[capId] = label; }
      figures.push({ label, text: (capText || '').replace(/<[^>]+>/g, ''), id: fig.id });
      p.replaceWith(fig);
    });

    // Cross-references (E05 §5.7.2)
    box.querySelectorAll('a.xref').forEach(a => {
      const id = a.getAttribute('href').slice(1);
      if (!targets[id]) { issues.push({ msg: `Cross-reference to #${id} has no target. Add {#${id}} to a heading or caption (E05 §5.7.2).`, field: 'f-body' }); a.textContent = '[missing reference]'; return; }
      if (a.dataset.mode === 'page') { a.classList.add('xref-page'); a.textContent = ''; } else a.textContent = targets[id];
    });

    // Starters and the body wrapper
    const kids = [...box.children];
    const firstH1 = kids.findIndex(e => e.tagName === 'H1');
    let lead = '';
    if (firstH1 !== 0 && kids.length) {
      const pre = document.createElement('div'); pre.className = 'startpage lead'; pre.dataset.start = '1';
      (firstH1 < 0 ? kids : kids.slice(0, firstH1)).forEach(k => pre.appendChild(k));
      box.prepend(pre);
    }

    // Revision history (E02 §5.1.3)
    const hist = parseBlock(f['f-history']);
    const ht = hist.querySelector('table');
    let histHtml = '';
    if (ht) {
      const label = nextLabel('Table', box);
      const c = document.createElement('caption'); c.innerHTML = `<b>${label}.</b> Revision history, newest first`; ht.prepend(c);
      ht.querySelectorAll('[align]').forEach(x => x.removeAttribute('align'));
      ht.querySelectorAll('tbody td:first-child').forEach(td => { td.innerHTML = `<code>${esc(td.textContent.replace(/`/g, '').trim())}</code>`; });
      ht.querySelectorAll('tbody tr').forEach((tr, r) => [...tr.children].forEach((td, ci) => { if (!td.textContent.trim()) issues.push({ msg: `Revision history, row ${r + 1}, column ${ci + 1}: the cell is blank. Enter None or — (C04 §5.4.1).`, field: 'f-history' }); }));
      ht.id = 'tbl-history';
      tables.push({ label, text: 'Revision history, newest first', id: 'tbl-history' });
      histHtml = ht.outerHTML;
    }

    // Lists of tables and figures, contents (E05 §5.8.2)
    const tocItems = toc.map(t => `<li class="l${t.lvl}"><span class="n">${t.num}</span><a href="#${t.id}">${esc(t.text)}</a></li>`).join('')
      + '<li class="l1"><span class="n"></span><a href="#rev">Revision History</a></li>';
    const lot = o['o-lot'] && tables.length ? `<section class="lot startpage" data-start="1"><h2 id="lot-h">List of Tables</h2><ol>${tables.map(t => `<li><span class="n">${esc(t.label)}</span><a href="#${t.id}">${esc(t.text)}</a></li>`).join('')}</ol></section>` : '';
    const lof = o['o-lof'] && figures.length ? `<section class="lot${lot ? '' : ' startpage'}"${lot ? '' : ' data-start="1"'}><h2 id="lof-h">List of Figures</h2><ol>${figures.map(t => `<li><span class="n">${esc(t.label)}</span><a href="#${t.id}">${esc(t.text)}</a></li>`).join('')}</ol></section>` : '';
    const dist = distRows.length ? `<section class="dist startpage" data-start="1"><h2>Distribution List</h2><table id="tbl-distribution"><caption><b>Table 1.</b> Distribution list</caption><thead><tr><th>Name</th><th>Role</th><th>Organization</th></tr></thead><tbody>${distRows.map(r => `<tr>${[0, 1, 2].map(i => `<td>${esc(r[i] || '')}</td>`).join('')}</tr>`).join('')}</tbody></table></section>` : '';

    // Mark starters in order and insert two-sided fillers (E05 §5.8.7)
    const lockupHdr = lockup;
    const wmText = o['o-watermark'] && st !== 'Approved' ? JSON.stringify(st.toUpperCase()) : '';
    const front = `${dist}<nav class="toc startpage" data-start="1" aria-label="Contents"><h2>Contents</h2><ol>${tocItems}</ol></nav>${lot}${lof}`;
    const html0 = `<div class="main">${front}${box.innerHTML}<section class="rev"><h1 id="rev" data-start="1"${o['o-section'] ? ' data-secname="Revision History"' : ''}>Revision History</h1>${histHtml}</section></div>`;
    const tpl = document.createElement('template'); tpl.innerHTML = html0;
    const starters = [...tpl.content.querySelectorAll('[data-start]')];
    starters.forEach((el, i) => { el.dataset.start = String(i); if (fillers && fillers.has(i)) el.insertAdjacentHTML('beforebegin', '<div class="filler">This page is intentionally left blank.</div>'); });
    const mainHtml = tpl.innerHTML;

    const meta = [
      ['Identifier', esc(f['f-identifier']), 'm'], ['Version', ver, 'm'], ['Status', esc(st), ''],
      ['Issue Date', esc(f['f-date']), 'm'], ['Owner', esc(f['f-owner']), ''], ['Approver', esc(f['f-approver']), '']
    ];
    if (st === 'Deprecated') meta.push(['Superseded By', esc(f['f-superseded']), 'm']);
    if (f['f-waiver'].trim()) { meta.push(['Waiver ID', esc(f['f-waiver']), 'm']); meta.push(['Waiver Expiry', esc(f['f-waiver-expiry']), 'm']); }

    const html = `
<div class="doc${wmText ? ' has-wm' : ''}" style="${stVars}${wmText ? ` --wm-text: ${esc(wmText)};` : ''}">
  <section class="cover" aria-label="Cover">
    <header class="chead">${lockup}<span class="badge"><i></i>${esc(st)}</span></header>
    ${bannerText ? `<div class="banner">${bannerText}</div>` : ''}
    <div class="titles" id="cover-titles">
      <div class="eyebrow">${esc(f['f-category'])}</div>
      <div class="dtitle">${esc(f['f-title'])}</div>
      <p class="dsub">${esc(f['f-subtitle'])}</p>
    </div>
    <div class="panel">
      <dl>${meta.map(m => `<div><dt>${m[0]}</dt><dd${m[2] ? ' class="m"' : ''}>${m[1] || '—'}</dd></div>`).join('')}</dl>
      <div class="cfoot">© ${esc(year)} Irvantri Standards Pte. Ltd. All rights reserved.</div>
    </div>
  </section>
  <div class="run-hdr-left" aria-hidden="true">${lockupHdr}</div>
  <div class="run-hdr-right" style="${stVars}"><span class="badge"><i></i>${esc(st)}</span>${bannerText ? `<div class="banner hb">${bannerText}</div>` : ''}</div>
  <div class="run-ftr-left">${esc(f['f-title'])}<span class="sep">|</span><code>${ver}</code></div>
  ${mainHtml}
  ${o['o-back'] ? `<section class="back" aria-label="Back page"><div class="bwrap">${lockup}<p>© ${esc(year)} Irvantri Standards Pte. Ltd. All rights reserved.</p></div></section>` : ''}
</div>`;
    return { html, issues, starters: starters.length };
  }

  // ------------------------------------------------------------------ paged rendering
  class Frame extends Paged.Handler {
    afterPageLayout(pageEl, page, breakToken, chunker) {
      // Repeat table header rows on continuation pages (E05 §5.4.4)
      pageEl.querySelectorAll('table[data-split-from]').forEach(t => {
        if (t.querySelector('thead')) return;
        const src = chunker.source.querySelector(`[data-ref="${t.getAttribute('data-ref')}"] > thead`);
        if (src) { const cap = t.querySelector('caption'); if (cap) cap.remove(); t.insertBefore(src.cloneNode(true), t.firstChild); }
      });
    }
  }
  Paged.registerHandlers(Frame);

  let busy = false, again = false, renderSeq = 0;
  async function layout(html) {
    const stage = $('stage');
    document.querySelectorAll('style[data-pagedjs-inserted-styles]').forEach(s => s.remove());
    stage.innerHTML = '';
    const previewer = new Paged.Previewer();
    const flow = await previewer.preview(html, [{ 'tpl-e01-06.css': $('doc-css').textContent }], stage);
    return flow;
  }
  function pageNo(el) { const p = el && el.closest('.pagedjs_page'); return p ? +p.dataset.pageNumber : 0; }

  async function preview() {
    if (busy) { again = true; return; }
    busy = true;
    const seq = ++renderSeq;
    setStatus('Laying out pages…');
    const t0 = performance.now();
    try {
      let built = buildDocument(null);
      await layout(built.html);
      if ($('o-twosided').checked) {
        // Each part starts on a right-hand (odd) page; insert intentionally blank pages where needed.
        const fillers = new Set();
        let shift = 0;
        document.querySelectorAll('#stage [data-start]').forEach(el => {
          const i = +el.dataset.start;
          if (fillers.has(i) || el.hasAttribute('data-split-from')) return;
          const pg = pageNo(el) + shift;
          if (pg && pg % 2 === 0) { fillers.add(i); shift++; }
        });
        if (fillers.size) { built = buildDocument(fillers); await layout(built.html); }
      }
      decorate();
      const issues = built.issues.concat(measureIssues());
      lastIssues = issues;
      if (pressView) pressify();
      showIssues();
      const total = document.querySelectorAll('#stage .pagedjs_page').length;
      setStatus(`${total} pages laid out in ${Math.round(performance.now() - t0)} ms.`);
      document.documentElement.dataset.ready = String(seq);
    } catch (err) {
      setStatus('The preview could not be laid out: ' + err.message);
      console.error(err);
    }
    busy = false;
    if (again) { again = false; preview(); }
  }

  function decorate() {
    const doc = document.querySelector('#stage .doc') || document;
    // Section name in the running header (E05 §5.9.1)
    if ($('o-section').checked) {
      let current = '';
      document.querySelectorAll('#stage .pagedjs_page').forEach(pg => {
        const h = pg.querySelector('h1[data-secname]');
        if (h) current = h.dataset.secname;
        if (h && h.hasAttribute('data-split-from')) return;
        const box = pg.querySelector('.pagedjs_margin-top-right .run-hdr-right');
        if (box && current) { const s = document.createElement('span'); s.className = 'secname'; s.textContent = current; box.appendChild(s); }
      });
    }
    // Page cross-references: write the resolved number as text so it has an accessible name (E05 §5.7.2)
    document.querySelectorAll('#stage a.xref-page').forEach(a => {
      const id = decodeURIComponent((a.getAttribute('href') || '').slice(1));
      const t = id && document.querySelector(`#stage [data-id="${CSS.escape(id)}"], #stage [id="${CSS.escape(id)}"]`);
      const n = pageNo(t);
      if (n) { a.textContent = String(n); a.classList.add('resolved'); }
    });
    document.querySelectorAll('#stage a.fn[data-footnote-call]').forEach((a, i) => a.setAttribute('aria-label', `Footnote ${i + 1}`));
    // Review watermark (E02 §5.3.3)
    const wm = document.querySelector('#stage .doc.has-wm');
    document.querySelectorAll('#stage .pagedjs_main_page').forEach(pg => pg.classList.toggle('wm', !!wm));
  }

  function measureIssues() {
    const out = [];
    const t = document.getElementById('cover-titles');
    if (t && t.scrollHeight > t.clientHeight + 1) out.push({ msg: 'The cover title and subtitle overflow their box. Shorten the title or the subtitle (E01 §5.5.5).', field: 'f-title' });
    const first = document.querySelector('#stage .pagedjs_main_page');
    if (first) {
      const f = first.querySelector('.run-ftr-left'), pn = first.querySelector('.pagedjs_margin-bottom-right');
      const area = first.querySelector('.pagedjs_area');
      const fr = f && document.createRange(); if (fr) fr.selectNodeContents(f);
      if (fr && area && fr.getBoundingClientRect().width > area.getBoundingClientRect().width - 34 * MM) out.push({ msg: 'The title is too long for the running footer. Shorten the document title (E01 §5.5.5).', field: 'f-title' });
      const hb = first.querySelector('.run-hdr-right');
      const marginTop = first.querySelector('.pagedjs_margin-top');
      if (hb && area && hb.getBoundingClientRect().bottom > area.getBoundingClientRect().top + 1) out.push({ msg: 'The running header text runs into the body. Shorten the status banner inputs or turn off the section name (E01 §5.5.5).', field: 'f-status' });
    }
    document.querySelectorAll('#stage .pagedjs_page').forEach(pg => {
      const area = pg.querySelector('.pagedjs_area');
      if (!area) return;
      const ar = area.getBoundingClientRect();
      pg.querySelectorAll('.pagedjs_area table:not(.land table), .pagedjs_area pre, .pagedjs_area figure').forEach(el => {
        if (el.closest('.land')) return;
        if (el.scrollWidth > el.clientWidth + 2 || el.getBoundingClientRect().right > ar.right + 2) {
          const lab = el.querySelector('caption b, figcaption b');
          out.push({ msg: `${lab ? lab.textContent.replace(/\.$/, '') : 'An element'} on page ${pg.dataset.pageNumber} is wider than the text block. ${el.tagName === 'TABLE' ? 'Add {landscape} to its caption or cut columns' : 'Make it narrower'} (E05 §5.4.8).`, field: 'f-body' });
        }
      });
      pg.querySelectorAll('.land').forEach(l => {
        const r = l.querySelector('.rot');
        if (r && (r.scrollHeight > 170 * MM + 2 || r.scrollWidth > 222 * MM + 2)) {
          const lab = r.querySelector('caption b');
          out.push({ msg: `${lab ? lab.textContent.replace(/\.$/, '') : 'A landscape table'} does not fit one rotated page. Split it into smaller tables (E05 §5.4.8).`, field: 'f-body' });
        }
      });
    });
    const seen = new Set();
    return out.filter(i => !seen.has(i.msg) && seen.add(i.msg));
  }

  function pressIssues() {
    const out = [];
    if ($('f-status').value !== 'Approved') out.push({ msg: 'Press files need Approved status. Draft and review documents stay digital (E03 §5.4.2).', field: 'f-status', press: true });
    const seen = new Set();
    document.querySelectorAll('#stage img[data-raster]').forEach(img => {
      const fig = img.closest('figure'); const lab = fig && fig.querySelector('figcaption b');
      const name = lab ? lab.textContent.replace(/\.$/, '') : 'A figure';
      if (seen.has(name)) return; seen.add(name);
      out.push({ msg: `${name} is a raster image. Press export takes SVG figures only, because colors are never converted automatically (E03 §5.3.1, E05 §5.6.2).`, field: 'f-body', press: true });
    });
    return out;
  }

  function allIssues(press) {
    const fe = fieldErrors();
    const list = Object.entries(fe).map(([id, msg]) => ({ msg, field: id }));
    return list.concat(lastIssues, press ? pressIssues() : []);
  }

  function showIssues(press) {
    const list = allIssues(press);
    const box = $('issues');
    if (!list.length) { box.innerHTML = '<p class="ok">No problems found. Both exports are ready.</p>'; return list; }
    box.innerHTML = '<ul></ul>';
    const ul = box.firstChild;
    list.forEach(i => {
      const li = document.createElement('li');
      if (i.press) li.className = 'press';
      li.textContent = i.msg + ' ';
      if (i.field) {
        const b = document.createElement('button'); b.type = 'button'; b.className = 'btn'; b.textContent = `Go to ${LABELS[i.field] || 'field'}`;
        b.style.minHeight = '28px'; b.style.padding = '2px 8px'; b.style.marginTop = '2px';
        b.addEventListener('click', () => { const el = $(i.field); el.closest('details').open = true; el.focus(); });
        li.appendChild(b);
      }
      ul.appendChild(li);
    });
    return list;
  }

  // ------------------------------------------------------------------ press layout (E01 §5.3.4, §5.5.7)
  function pressify() {
    if (document.querySelector('#stage .press-sheet')) return;
    const add = (sheet, cls, l, t, w, h) => { const i = document.createElement('i'); i.className = cls; Object.assign(i.style, { left: l + 'mm', top: t + 'mm', width: w + 'mm', height: h + 'mm' }); sheet.appendChild(i); };
    document.querySelectorAll('#stage .pagedjs_page').forEach(pg => {
      const sheet = document.createElement('div'); sheet.className = 'press-sheet';
      pg.parentNode.insertBefore(sheet, pg); sheet.appendChild(pg);
      if (pg.classList.contains('pagedjs_first_page')) { // cover spine bleed
        add(sheet, 'bl-deep', 7, 7, 7, 228.72); add(sheet, 'bl-accent', 7, 235.72, 7, 74.28);
      } else if (pg.classList.contains('pagedjs_main_page')) { // top accent bar bleed: 24% / 76% of the 210 mm trim
        add(sheet, 'bl-accent', 7, 7, 53.4, 5); add(sheet, 'bl-deep', 60.4, 7, 162.6, 5);
      }
      [[0, 10, 'h'], [10, 0, 'v'], [223, 10, 'h'], [220, 0, 'v'], [0, 307, 'h'], [10, 310, 'v'], [223, 307, 'h'], [220, 310, 'v']].forEach(([l, t, k]) => {
        const i = document.createElement('i'); i.className = 'crop-' + k; i.style.left = l + 'mm'; i.style.top = t + 'mm'; sheet.appendChild(i);
      });
    });
  }
  function unpressify() {
    document.querySelectorAll('#stage .press-sheet').forEach(sheet => { const pg = sheet.querySelector('.pagedjs_page'); sheet.parentNode.insertBefore(pg, sheet); sheet.remove(); });
  }
  const PRESS_CSS = '@page { size: 230mm 317mm; margin: 0 !important; } html.press-print, html.press-print body { width: 230mm !important; height: auto !important; min-height: 0 !important; max-height: none !important; } '
    + 'html.press-print .pagedjs_pages { height: auto !important; max-height: none !important; } '
    + 'html.press-print .press-sheet > .pagedjs_page, html.press-print .press-sheet .pagedjs_sheet { width: 210mm !important; height: 297mm !important; min-height: 297mm !important; max-height: 297mm !important; break-after: auto !important; page-break-after: auto !important; }';

  // ------------------------------------------------------------------ exports
  function blockExport(list) {
    $('issues').closest('section').scrollIntoView({ block: 'nearest' });
    announce(`Export stopped. ${list.length} ${list.length === 1 ? 'item needs' : 'items need'} fixing; see Export checks.`);
    const firstBtn = $('issues').querySelector('button'); if (firstBtn) firstBtn.focus();
  }
  function withTitle(fn) {
    const old = document.title;
    const f = collect().fields;
    document.title = `${f['f-identifier'].trim()} ${f['f-title'].trim()} ${f['f-version'].trim()}`.trim();
    const done = () => { document.title = old; window.removeEventListener('afterprint', done); };
    window.addEventListener('afterprint', done);
    fn();
  }
  async function exportDigital() {
    FIELDS.forEach(id => touched.add(id)); showFieldErrors(true);
    if (pressView) togglePressView(false);
    await settle();
    const list = showIssues(false);
    if (list.length) return blockExport(list);
    withTitle(() => window.print());
  }
  async function exportPress() {
    FIELDS.forEach(id => touched.add(id)); showFieldErrors(true);
    await settle();
    const list = showIssues(true);
    if (list.length) return blockExport(list);
    pressify();
    const style = document.createElement('style'); style.id = 'press-print'; style.textContent = PRESS_CSS; document.head.appendChild(style);
    document.documentElement.classList.add('press-print');
    const done = () => {
      style.remove(); document.documentElement.classList.remove('press-print');
      if (!pressView) unpressify();
      window.removeEventListener('afterprint', done);
    };
    window.addEventListener('afterprint', done);
    withTitle(() => window.print());
  }
  function togglePressView(on) {
    pressView = on == null ? !pressView : on;
    $('btn-press-preview').setAttribute('aria-pressed', String(pressView));
    document.documentElement.classList.toggle('press-view', pressView);
    if (pressView) pressify(); else unpressify();
    announce(pressView ? 'Press preview on: pages show the 3 mm bleed and crop marks.' : 'Press preview off.');
  }
  async function settle() { clearTimeout(timer); await preview(); while (busy) await new Promise(r => setTimeout(r, 50)); }

  // Filled Copy (E01 §5.5.6)
  function saveFilledCopy() {
    const json = JSON.stringify(collect()).replace(/</g, '\\u003c');
    const html = PRISTINE.replace(new RegExp('(<scr' + 'ipt type="application/json" id="filled-state">)[\\s\\S]*?(</scr' + 'ipt>)'), (_, a, b) => a + json + b);
    const f = collect().fields;
    const slug = (f['f-identifier'] || 'Document').trim().replace(/[^\w-]+/g, '-') + '_' + (f['f-version'] || '').trim();
    const a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([html], { type: 'text/html' }));
    a.download = `${slug}_Filled-Copy.html`;
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(() => URL.revokeObjectURL(a.href), 4000);
    dirty = false;
    try { localStorage.removeItem(STORE_KEY); } catch (e) { /* storage unavailable */ }
    announce(`Filled copy saved as ${a.download}. Open it in a browser to keep editing.`);
  }

  // ------------------------------------------------------------------ paste from Word and Google Docs (E05 §5.1.4)
  const td = new TurndownService({ headingStyle: 'atx', bulletListMarker: '-', codeBlockStyle: 'fenced', emDelimiter: '*', strongDelimiter: '**' });
  td.use(turndownPluginGfm.gfm);
  td.remove(['style', 'script', 'meta', 'title', 'link', 'xml']);
  td.addRule('sup', { filter: ['sup'], replacement: c => c.trim() ? `^${c.trim()}^` : '' });
  td.addRule('sub', { filter: ['sub'], replacement: c => c.trim() ? `~${c.trim()}~` : '' });
  td.addRule('underline', { filter: ['u', 'ins'], replacement: c => c });
  td.addRule('font', { filter: ['font', 'mark'], replacement: c => c });
  function cleanPastedHtml(html) {
    const doc = new DOMParser().parseFromString(html, 'text/html');
    // Google Docs wraps content in <b style="font-weight:normal">; Word marks bold and italic with spans.
    doc.querySelectorAll('b, strong').forEach(b => { if (/font-weight:\s*(normal|400)/i.test(b.getAttribute('style') || '')) b.replaceWith(...b.childNodes); });
    doc.querySelectorAll('span').forEach(s => {
      const st = s.getAttribute('style') || '';
      let node = null;
      if (/font-weight:\s*(bold|[6-9]00)/i.test(st)) node = doc.createElement('strong');
      if (/font-style:\s*italic/i.test(st)) { const em = doc.createElement('em'); if (node) node.appendChild(em); else node = em; }
      if (/vertical-align:\s*super/i.test(st)) node = doc.createElement('sup');
      if (/vertical-align:\s*sub/i.test(st)) node = doc.createElement('sub');
      if (node) { const inner = node.querySelector('em') || node; inner.append(...s.childNodes); s.replaceWith(node); }
    });
    // Word list paragraphs (mso-list) become real lists.
    let list = null, lastLevel = 0, stack = [];
    [...doc.body.querySelectorAll('p')].forEach(p => {
      const st = p.getAttribute('style') || '';
      const lv = /mso-list:\s*\w+\s+level(\d)/i.exec(st);
      if (!lv) { stack = []; return; }
      const level = +lv[1];
      const marker = p.querySelector('[style*="mso-list:Ignore"], [style*="mso-list: Ignore"]');
      const mtext = marker ? marker.textContent.trim() : '';
      if (marker) marker.remove();
      const ordered = /^(\d+|[a-z]|[ivx]+)[.)]$/i.test(mtext);
      const li = doc.createElement('li'); li.append(...p.childNodes);
      while (stack.length > level) stack.pop();
      while (stack.length < level) {
        const l = doc.createElement(ordered ? 'ol' : 'ul');
        if (stack.length) { const parentLi = stack[stack.length - 1].lastElementChild || stack[stack.length - 1].appendChild(doc.createElement('li')); parentLi.appendChild(l); }
        else p.parentNode.insertBefore(l, p);
        stack.push(l);
      }
      stack[stack.length - 1].appendChild(li);
      p.remove();
    });
    // Tables: first row becomes the header row so the table converts to Markdown.
    doc.querySelectorAll('table').forEach(t => {
      if (!t.querySelector('th')) {
        const tr = t.querySelector('tr');
        if (tr) { const thead = doc.createElement('thead'); const ntr = doc.createElement('tr'); [...tr.children].forEach(c => { const th = doc.createElement('th'); th.innerHTML = c.innerHTML; ntr.appendChild(th); }); thead.appendChild(ntr); tr.remove(); t.prepend(thead); }
      }
      t.querySelectorAll('[colspan], [rowspan]').forEach(c => { const n = (+c.getAttribute('colspan') || 1) - 1; c.removeAttribute('colspan'); c.removeAttribute('rowspan'); for (let i = 0; i < n; i++) c.after(doc.createElement(c.tagName)); });
      t.querySelectorAll('td p, th p').forEach(p => { p.replaceWith(...p.childNodes, ' '); });
    });
    // Images that are not embedded cannot be kept offline.
    doc.querySelectorAll('img').forEach(img => { const src = img.getAttribute('src') || ''; if (!/^data:image\//.test(src)) img.replaceWith(doc.createTextNode(`[Image not embedded: add it with Add image${img.alt ? ` (${img.alt})` : ''}]`)); });
    doc.querySelectorAll('[style], [class], [face], [color], [size]').forEach(el => { ['style', 'class', 'face', 'color', 'size'].forEach(a => el.removeAttribute(a)); });
    return doc.body.innerHTML;
  }
  async function onPaste(e) {
    const dt = e.clipboardData;
    if (!dt) return;
    const files = [...(dt.files || [])].filter(f => /^image\/(png|jpeg|svg\+xml)$/.test(f.type));
    const html = dt.getData('text/html');
    if (!html && !files.length) return;
    e.preventDefault();
    const ta = e.target;
    let text = '';
    if (html) {
      text = td.turndown(cleanPastedHtml(html.replace(/<!--[\s\S]*?-->/g, '')));
      // Embedded images: move them into the image store and reference them by name.
      const found = [];
      text = text.replace(/!\[([^\]]*)\]\((data:image\/[^)\s]+)\)/g, (_, alt, src) => { const name = `pasted-${Date.now()}-${found.length + 1}.${/png/.test(src) ? 'png' : /svg/.test(src) ? 'svg' : 'jpg'}`; found.push({ name, src }); return `![${alt}](${name} "Caption")`; });
      for (const it of found) {
        const type = it.src.slice(5, it.src.indexOf(';'));
        const blob = await (await fetch(it.src)).blob();
        await addImageFile(new File([blob], it.name, { type }));
      }
    } else {
      for (const f of files) { const name = await addImageFile(f); if (name) text += `\n![Describe the image](${name} "Caption")\n`; }
    }
    ta.setRangeText(text, ta.selectionStart, ta.selectionEnd, 'end');
    markDirty(); schedule();
    announce('Pasted content converted to Markdown. Check headings, captions and alternative text.');
  }

  // ------------------------------------------------------------------ snippets
  const SNIPPETS = {
    table: '\nTable: Caption describing the table {#tbl-name}\n\n| Item | Amount (SGD) |\n| :--- | ---: |\n| Item one | 0.00 |\n| Total | 0.00 |\n\nSource: Where the numbers come from.\n',
    callout: '\n> [!NOTE]\n> Callout text. Other types: [!TIP], [!IMPORTANT], [!WARNING], [!CAUTION].\n',
    code: '\n```text {lines}\ncode\n```\n',
    quote: '\n> Quoted text.\n>\n> — Source\n',
    figure: '\n![Describe what the image shows](image-name.svg "Caption {#fig-name}")\n',
    footnote: '[^1]\n\n[^1]: Footnote text.\n',
    clause: '\n**5.1.1** The clause text, using SHALL, SHOULD or MAY.\n',
    signoff: '\n```signoff\nName: Full name\nRole: Role\nDate: YYYY-MM-DD\n```\n',
    appendix: '\n# Appendix A — Title\n\n## First section\n\nText.\n',
    break: '\n\\pagebreak\n'
  };

  // ------------------------------------------------------------------ wiring
  let timer;
  function schedule() { clearTimeout(timer); timer = setTimeout(preview, 700); }
  function setStatus(t) { $('status-line').textContent = t; }
  function announce(t) { $('live').textContent = ''; setTimeout(() => { $('live').textContent = t; }, 30); }
  let autosaveTimer;
  function markDirty() {
    dirty = true;
    clearTimeout(autosaveTimer);
    autosaveTimer = setTimeout(() => { try { localStorage.setItem(STORE_KEY, JSON.stringify({ at: new Date().toISOString(), state: collect() })); } catch (e) { /* storage full or blocked */ } }, 1000);
  }

  FIELDS.concat(OPTIONS).forEach(id => {
    const el = $(id);
    el.addEventListener('input', () => { markDirty(); schedule(); if (touched.has(id)) showFieldErrors(); });
    el.addEventListener('change', () => { markDirty(); schedule(); showFieldErrors(); });
    el.addEventListener('blur', () => { touched.add(id); showFieldErrors(); });
  });
  $('f-body').addEventListener('paste', onPaste);
  document.querySelectorAll('[data-ins]').forEach(b => b.addEventListener('click', () => {
    const ta = $('f-body');
    ta.setRangeText(SNIPPETS[b.dataset.ins], ta.selectionStart, ta.selectionEnd, 'end');
    ta.focus(); markDirty(); schedule();
  }));
  $('btn-add-image').addEventListener('click', () => $('f-image').click());
  $('f-image').addEventListener('change', async (e) => {
    const names = [];
    for (const f of e.target.files) { const n = await addImageFile(f); if (n) names.push(n); }
    e.target.value = '';
    if (names.length) { announce(`Added ${names.join(', ')}. Refer to ${names.length > 1 ? 'them' : 'it'} in the body by name.`); schedule(); }
  });
  $('btn-save').addEventListener('click', saveFilledCopy);
  $('btn-pdf').addEventListener('click', exportDigital);
  $('btn-press').addEventListener('click', exportPress);
  $('btn-press-preview').addEventListener('click', () => togglePressView());
  window.addEventListener('beforeunload', (e) => { if (dirty) { e.preventDefault(); e.returnValue = ''; } });

  // Start: a Filled Copy restores its values; otherwise the sample loads, and autosaved work is offered.
  const filled = JSON.parse($('filled-state').textContent || 'null');
  apply(filled || sampleState());
  let saved = null;
  try { saved = JSON.parse(localStorage.getItem(STORE_KEY) || 'null'); } catch (e) { saved = null; }
  if (saved && saved.state) {
    $('restore').hidden = false;
    $('restore-text').textContent = `Unsaved work from ${saved.at ? saved.at.slice(0, 16).replace('T', ' ') + ' UTC' : 'an earlier session'} was found in this browser.`;
    $('btn-restore').addEventListener('click', () => { apply(saved.state); $('restore').hidden = true; dirty = true; preview(); announce('Unsaved work restored.'); });
    $('btn-discard').addEventListener('click', () => { try { localStorage.removeItem(STORE_KEY); } catch (e) { /* ignore */ } $('restore').hidden = true; announce('Unsaved work discarded.'); });
  }
  window.__tpl = { preview, collect, apply, buildDocument, allIssues, pressify, unpressify, exportDigital, exportPress, togglePressView, saveFilledCopy, PRESS_CSS, addImageFile, onPaste, cleanPastedHtml, td };
  document.fonts.ready.then(preview);
})();
