(function () {
  var FLAGS = {
    'Sweden': 'sweden', 'Finland': 'finland', 'United Kingdom': 'united-kingdom', 'Norway': 'norway',
    'Netherlands': 'netherlands', 'Denmark': 'denmark', 'Italy': 'italy', 'Switzerland': 'switzerland',
    'Malaysia': 'malaysia', 'Belgium': 'belgium', 'Spain': 'spain', 'Turkey': 'turkey', 'Thailand': 'thailand',
    'Egypt': 'egypt', 'Tunisia': 'tunisia', 'France': 'france', 'Monaco': 'monaco', 'Libya': 'libya',
    'Germany': 'germany', 'Poland': 'poland', 'Albania': 'albania', 'Canary Islands': 'canary-islands'
  };
  var IDS = { '752': 'Sweden', '246': 'Finland', '826': 'United Kingdom', '578': 'Norway', '528': 'Netherlands',
    '208': 'Denmark', '380': 'Italy', '756': 'Switzerland', '458': 'Malaysia', '056': 'Belgium', '724': 'Spain',
    '792': 'Turkey', '764': 'Thailand', '818': 'Egypt', '788': 'Tunisia', '250': 'France', '434': 'Libya',
    '276': 'Germany', '616': 'Poland', '008': 'Albania' };
  var PINS = { 'Monaco': [7.42, 43.74], 'Canary Islands': [-15.6, 28.3] };

  var wrap = document.getElementById('travel-map');
  var tip = document.getElementById('map-tip');
  var chips = Array.prototype.slice.call(document.querySelectorAll('.flag-chip'));
  var loading = wrap.querySelector('.map-loading');

  function fail() { loading.textContent = 'Map unavailable right now. The list shows every country.'; }
  if (!window.d3 || !window.topojson) { fail(); return; }

  d3.json('https://cdn.jsdelivr.net/npm/world-atlas@2.0.2/countries-110m.json').then(function (world) {
    loading.remove();
    var W = 960, H = 600;
    var features = topojson.feature(world, world.objects.countries).features
      .filter(function (f) { return f.properties.name !== 'Antarctica' && f.properties.name !== 'Fiji'; });
    var nameOf = function (f) { return IDS[f.id] || (FLAGS[f.properties.name] ? f.properties.name : null); };

    var proj = d3.geoNaturalEarth1().fitExtent([[10, 10], [W - 10, H - 10]],
      { type: 'MultiPoint', coordinates: [[-20, 70], [114, 70], [-20, -4], [114, -4]] });
    var path = d3.geoPath(proj);

    var svg = d3.select(wrap).insert('svg', ':first-child')
      .attr('viewBox', '0 0 ' + W + ' ' + H).attr('preserveAspectRatio', 'xMidYMid slice');
    var g = svg.append('g');

    var shapes = {};
    g.selectAll('path').data(features).join('path')
      .attr('d', path)
      .attr('class', function (f) { return nameOf(f) ? 'land visited' : 'land'; })
      .each(function (f) { var n = nameOf(f); if (n) shapes[n] = this; });

    Object.keys(PINS).forEach(function (n) {
      var p = proj(PINS[n]);
      shapes[n] = g.append('circle').attr('class', 'pin').attr('cx', p[0]).attr('cy', p[1]).attr('r', 5)
        .datum({ pin: n }).node();
    });

    function showTip(name, evt) {
      var r = wrap.getBoundingClientRect();
      tip.innerHTML = '<img src="/flags/' + FLAGS[name] + '.webp" alt="">' + name;
      tip.style.left = (evt.clientX - r.left) + 'px';
      tip.style.top = (evt.clientY - r.top) + 'px';
      tip.hidden = false;
    }
    function tipAtShape(name) {
      var el = shapes[name]; if (!el) return;
      var b = el.getBoundingClientRect();
      showTip(name, { clientX: b.left + b.width / 2, clientY: b.top + b.height / 2 });
    }
    function highlight(name, on) {
      if (shapes[name]) shapes[name].classList.toggle('hl', on);
      chips.forEach(function (c) { c.classList.toggle('hl', on && c.dataset.country === name); });
    }

    g.selectAll('.visited, .pin')
      .on('pointermove', function (evt, d) { var n = d.pin || nameOf(d); highlight(n, true); showTip(n, evt); })
      .on('pointerleave', function (evt, d) { highlight(d.pin || nameOf(d), false); tip.hidden = true; });

    var zoom = d3.zoom().scaleExtent([1, 8])
      .translateExtent([[0, 0], [W, H]])
      .filter(function (evt) { return evt.type !== 'wheel' && evt.type !== 'dblclick'; })
      .on('zoom', function (evt) { g.attr('transform', evt.transform); tip.hidden = true; });
    svg.call(zoom);

    wrap.querySelectorAll('[data-zoom]').forEach(function (b) {
      b.addEventListener('click', function () {
        var k = b.dataset.zoom;
        if (k === 'in') svg.transition().duration(250).call(zoom.scaleBy, 1.6);
        else if (k === 'out') svg.transition().duration(250).call(zoom.scaleBy, 1 / 1.6);
        else svg.transition().duration(350).call(zoom.transform, d3.zoomIdentity);
      });
    });

    chips.forEach(function (c) {
      var n = c.dataset.country;
      c.addEventListener('mouseenter', function () { highlight(n, true); tipAtShape(n); });
      c.addEventListener('mouseleave', function () { highlight(n, false); tip.hidden = true; });
      c.addEventListener('focus', function () { highlight(n, true); tipAtShape(n); });
      c.addEventListener('blur', function () { highlight(n, false); tip.hidden = true; });
      c.addEventListener('click', function () {
        var el = shapes[n]; if (!el) return;
        var bb = el.getBBox(), cx = bb.x + bb.width / 2, cy = bb.y + bb.height / 2;
        var k = Math.min(6, Math.max(2, 0.35 / Math.max(bb.width / W, bb.height / H)));
        svg.transition().duration(500)
          .call(zoom.transform, d3.zoomIdentity.translate(W / 2, H / 2).scale(k).translate(-cx, -cy))
          .on('end', function () { highlight(n, true); tipAtShape(n); });
      });
    });
  }).catch(fail);
})();
