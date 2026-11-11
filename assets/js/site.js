(function () {
  var root = document.documentElement;
  var stored = null;
  try { stored = localStorage.getItem('theme'); } catch (e) {}
  if (stored) root.setAttribute('data-theme', stored);
  document.getElementById('theme-btn').addEventListener('click', function () {
    var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('theme', next); } catch (e) {}
  });

  var menuBtn = document.getElementById('menu-btn');
  var links = document.getElementById('nav-links');
  menuBtn.addEventListener('click', function () {
    var open = links.classList.toggle('open');
    menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  links.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') { links.classList.remove('open'); menuBtn.setAttribute('aria-expanded', 'false'); }
  });

  var buttons = document.querySelectorAll('.filters button');
  var yearSel = document.getElementById('year-filter');
  var typeF = 'all';
  function applyPubFilter() {
    var y = yearSel ? yearSel.value : 'all';
    document.querySelectorAll('.pub').forEach(function (p) {
      var okType = typeF === 'all' || p.getAttribute('data-t') === typeF;
      var okYear = y === 'all' || p.querySelector('.year').textContent.trim() === y;
      p.hidden = !(okType && okYear);
    });
  }
  buttons.forEach(function (b) {
    b.addEventListener('click', function () {
      buttons.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      typeF = b.getAttribute('data-f');
      applyPubFilter();
    });
  });
  if (yearSel) yearSel.addEventListener('change', applyPubFilter);

  var toTop = document.getElementById('to-top');
  window.addEventListener('scroll', function () {
    toTop.classList.toggle('show', window.scrollY > 600);
  }, { passive: true });
  toTop.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });

  var navLinks = links.querySelectorAll('a');
  var sections = ['education', 'research', 'publications', 'projects', 'resume'].map(function (id) { return document.getElementById(id); });
  window.addEventListener('scroll', function () {
    var current = 'top';
    sections.forEach(function (s) { if (s && s.getBoundingClientRect().top < 120) current = s.id; });
    navLinks.forEach(function (a) {
      if (a.getAttribute('href') === '#' + current) a.setAttribute('aria-current', 'page');
      else a.removeAttribute('aria-current');
    });
  }, { passive: true });
})();
