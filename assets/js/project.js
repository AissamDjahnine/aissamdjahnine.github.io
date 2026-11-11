(function () {
  var root = document.documentElement;
  try { var t = localStorage.getItem('theme'); if (t) root.setAttribute('data-theme', t); } catch (e) {}
  var themeBtn = document.getElementById('theme-btn');
  if (themeBtn) themeBtn.addEventListener('click', function () {
    var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('theme', next); } catch (e) {}
  });

  document.querySelectorAll('.bib .copy').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var code = btn.parentNode.querySelector('code');
      var done = function () { btn.textContent = 'Copied'; setTimeout(function () { btn.textContent = 'Copy'; }, 1500); };
      if (navigator.clipboard && code) navigator.clipboard.writeText(code.textContent).then(done, function () { btn.textContent = 'Select and copy'; });
      else btn.textContent = 'Select and copy';
    });
  });

  var links = Array.prototype.slice.call(document.querySelectorAll('.toc a'));
  var secs = links.map(function (a) { return document.getElementById(a.getAttribute('href').slice(1)); }).filter(Boolean);
  window.addEventListener('scroll', function () {
    var cur = null;
    secs.forEach(function (s) { if (s.getBoundingClientRect().top < 140) cur = s.id; });
    links.forEach(function (a) { a.classList.toggle('on', a.getAttribute('href') === '#' + cur); });
  }, { passive: true });

  function num(text) {
    var m = String(text).replace(/,/g, '').match(/-?\d+(\.\d+)?/);
    return m ? parseFloat(m[0]) : null;
  }
  function isNumericCell(td) {
    var t = td.textContent.trim();
    return /^-?\d[\d,]*(\.\d+)?\s*%?(\s*±\s*[\d.]+)?$/.test(t);
  }

  document.querySelectorAll('table[data-chart]').forEach(function (table) {
    var heads = Array.prototype.map.call(table.querySelectorAll('thead th'), function (th) { return th.textContent.trim(); });
    var rows = Array.prototype.slice.call(table.querySelectorAll('tbody tr'));
    var numericCols = [];
    for (var c = 1; c < heads.length; c++) {
      var ok = rows.every(function (r) { var cell = r.children[c]; return cell && isNumericCell(cell); });
      if (ok && !/perceptual|cases|scans/i.test(heads[c])) numericCols.push(c);
    }
    if (!numericCols.length) return;
    var data = rows.map(function (r) {
      var cells = Array.prototype.slice.call(r.children);
      var sub = cells.slice(1).filter(function (_, i) { return numericCols.indexOf(i + 1) === -1; })
        .map(function (td, i) { return td.textContent.trim(); }).filter(Boolean);
      var subLabels = [];
      cells.slice(1).forEach(function (td, i) {
        if (numericCols.indexOf(i + 1) === -1 && !/p-value|CI|cases/i.test(heads[i + 1])) subLabels.push(heads[i + 1] + ': ' + td.textContent.trim());
      });
      return {
        name: cells[0].textContent.trim(),
        sub: subLabels.join(' · '),
        cells: cells,
        strong: cells.map(function (td) { return !!td.querySelector('strong'); })
      };
    });

    var wrap = document.createElement('div');
    var top = document.createElement('div'); top.className = 'results-top';
    var cap = document.createElement('span'); cap.className = 'cap';
    var caption = table.querySelector('caption');
    cap.textContent = caption ? caption.textContent : '';
    top.appendChild(cap);
    var seg = document.createElement('div'); seg.className = 'seg'; seg.setAttribute('role', 'group'); seg.setAttribute('aria-label', 'Choose metric');
    if (numericCols.length > 1) top.appendChild(seg);
    var bars = document.createElement('div'); bars.className = 'bars'; bars.setAttribute('aria-live', 'polite');
    wrap.appendChild(top); wrap.appendChild(bars);

    function render(col) {
      var vals = data.map(function (d) { return num(d.cells[col].textContent); });
      var max = Math.max.apply(null, vals);
      var pct = data.some(function (d) { return /%/.test(d.cells[col].textContent); }) || /%|accuracy/i.test(heads[col]) && max > 1;
      var hi = max <= 1 ? 1 : (pct || max <= 100 ? 100 : max * 1.1);
      var anyStrong = data.some(function (d) { return d.strong[col]; });
      bars.innerHTML = data.map(function (d, i) {
        var v = vals[i];
        var lower = /distance|loss|error/i.test(heads[col]);
        var best = anyStrong ? d.strong[col] : v === (lower ? Math.min.apply(null, vals) : max);
        var w = Math.max(2, v / hi * 100);
        return '<div class="bar-row' + (best ? ' best' : '') + '">' +
          '<span class="name">' + d.name + (d.sub ? '<span class="fam">' + d.sub + '</span>' : '') + '</span>' +
          '<div class="bar-track"><div class="bar-fill" style="width:' + w.toFixed(1) + '%"></div></div>' +
          '<span class="val">' + d.cells[col].textContent.trim() + '</span></div>';
      }).join('');
    }
    numericCols.forEach(function (c, i) {
      var b = document.createElement('button'); b.type = 'button'; b.textContent = heads[c];
      b.setAttribute('aria-pressed', i === 0 ? 'true' : 'false');
      b.addEventListener('click', function () {
        seg.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        render(c);
      });
      seg.appendChild(b);
    });
    render(numericCols[0]);

    var card = table.closest('.results-card');
    var scroller = table.closest('.table-scroll');
    var details = document.createElement('details'); details.className = 'table';
    var summary = document.createElement('summary'); summary.textContent = 'Show the full table';
    details.appendChild(summary);
    scroller.parentNode.insertBefore(wrap, scroller);
    scroller.parentNode.insertBefore(details, scroller);
    details.appendChild(scroller);
    if (caption) caption.classList.add('note');
  });
})();
