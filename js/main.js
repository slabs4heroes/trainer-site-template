(function () {
  'use strict';
  var d = document, root = d.documentElement, body = d.body;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  root.classList.remove('no-js'); root.classList.add('js');

  /* ---------- scroll progress, nav hide/solid ---------- */
  var bar = d.querySelector('.bar'), nav = d.querySelector('.nav');
  var lastY = 0, ticking = false;
  function onScroll() {
    var y = window.scrollY || 0;
    var h = root.scrollHeight - window.innerHeight;
    if (bar) bar.style.transform = 'scaleX(' + (h > 0 ? Math.min(y / h, 1) : 0) + ')';
    if (nav) {
      nav.classList.toggle('solid', y > 30);
      var menuOpen = body.classList.contains('menu-open');
      nav.classList.toggle('hide', !menuOpen && y > lastY + 6 && y > 320);
      if (y < lastY - 6 || y < 320) nav.classList.remove('hide');
    }
    lastY = y; ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; requestAnimationFrame(onScroll); }
  }, { passive: true });
  onScroll();

  /* ---------- mobile menu ---------- */
  var burger = d.querySelector('.burger');
  function setMenu(open) {
    body.classList.toggle('menu-open', open);
    body.classList.toggle('noscroll', open);
    if (burger) { burger.setAttribute('aria-expanded', open ? 'true' : 'false'); burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu'); }
  }
  if (burger) burger.addEventListener('click', function () { setMenu(!body.classList.contains('menu-open')); });
  d.querySelectorAll('.menu a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
  d.addEventListener('keydown', function (e) { if (e.key === 'Escape') { setMenu(false); closeLb(); } });

  /* ---------- reveal on scroll ---------- */
  var rvs = d.querySelectorAll('.rv');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
    rvs.forEach(function (el) { io.observe(el); });
  } else { rvs.forEach(function (el) { el.classList.add('in'); }); }

  /* ---------- count-up numbers ---------- */
  function countUp(el) {
    var to = parseFloat(el.getAttribute('data-to')), suf = el.getAttribute('data-suf') || '';
    if (reduce) { el.textContent = to + suf; return; }
    var t0 = null, dur = 1500;
    function step(t) {
      if (!t0) t0 = t;
      var p = Math.min((t - t0) / dur, 1), e = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(to * e) + suf;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  var counts = d.querySelectorAll('[data-to]');
  if ('IntersectionObserver' in window) {
    var cio = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { countUp(e.target); cio.unobserve(e.target); } });
    }, { threshold: 0.6 });
    counts.forEach(function (el) { cio.observe(el); });
  } else { counts.forEach(function (el) { el.textContent = el.getAttribute('data-to') + (el.getAttribute('data-suf') || ''); }); }

  /* ---------- program tabs ---------- */
  var tabs = Array.prototype.slice.call(d.querySelectorAll('[role=tab]'));
  var panels = Array.prototype.slice.call(d.querySelectorAll('[role=tabpanel]'));
  function selectTab(tab, focus) {
    tabs.forEach(function (t) { t.setAttribute('aria-selected', t === tab ? 'true' : 'false'); t.tabIndex = t === tab ? 0 : -1; });
    panels.forEach(function (p) {
      var on = p.id === tab.getAttribute('aria-controls');
      p.hidden = !on; p.classList.remove('go');
      if (on) { void p.offsetWidth; requestAnimationFrame(function () { p.classList.add('go'); }); }
    });
    if (focus) tab.focus();
  }
  tabs.forEach(function (t, i) {
    t.addEventListener('click', function () { selectTab(t); });
    t.addEventListener('keydown', function (e) {
      var n = null;
      if (e.key === 'ArrowRight') n = tabs[(i + 1) % tabs.length];
      if (e.key === 'ArrowLeft') n = tabs[(i - 1 + tabs.length) % tabs.length];
      if (n) { e.preventDefault(); selectTab(n, true); }
    });
  });
  var firstPanel = panels.filter(function (p) { return !p.hidden; })[0];
  if (firstPanel && 'IntersectionObserver' in window) {
    var pio = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { panels.forEach(function (p) { if (!p.hidden) p.classList.add('go'); }); pio.disconnect(); } });
    }, { threshold: 0.15 });
    pio.observe(firstPanel);
  } else if (firstPanel) { firstPanel.classList.add('go'); }

  /* ---------- lightbox ---------- */
  var lb = d.querySelector('.lb'), lbImg = lb && lb.querySelector('img');
  function closeLb() { if (lb) lb.classList.remove('on'); }
  d.querySelectorAll('.gal figure').forEach(function (f) {
    f.addEventListener('click', function () {
      var im = f.querySelector('img'); if (!im || !lb) return;
      lbImg.src = im.currentSrc || im.src; lbImg.alt = im.alt; lb.classList.add('on');
    });
  });
  if (lb) lb.addEventListener('click', closeLb);

  /* ---------- desktop-only polish ---------- */
  if (fine && !reduce) {
    var spotRaf = null;
    d.addEventListener('pointermove', function (e) {
      if (spotRaf) return;
      spotRaf = requestAnimationFrame(function () {
        root.style.setProperty('--mx', e.clientX + 'px'); root.style.setProperty('--my', e.clientY + 'px'); spotRaf = null;
      });
    }, { passive: true });

    d.querySelectorAll('.card').forEach(function (c) {
      c.addEventListener('pointermove', function (e) {
        var r = c.getBoundingClientRect();
        c.style.setProperty('--x', (e.clientX - r.left) + 'px'); c.style.setProperty('--y', (e.clientY - r.top) + 'px');
      });
    });

    var hero = d.querySelector('.hero'), lw = d.querySelector('.logo-wrap');
    if (hero && lw) {
      hero.addEventListener('pointermove', function (e) {
        var r = hero.getBoundingClientRect();
        var px = (e.clientX - r.left) / r.width - 0.5, py = (e.clientY - r.top) / r.height - 0.5;
        lw.style.transform = 'rotateY(' + (px * 14) + 'deg) rotateX(' + (-py * 12) + 'deg)';
      });
      hero.addEventListener('pointerleave', function () { lw.style.transform = ''; });
    }

    d.querySelectorAll('.mag').forEach(function (m) {
      m.addEventListener('pointermove', function (e) {
        var r = m.getBoundingClientRect();
        m.style.transform = 'translate(' + ((e.clientX - r.left - r.width / 2) * 0.18) + 'px,' + ((e.clientY - r.top - r.height / 2) * 0.28) + 'px)';
      });
      m.addEventListener('pointerleave', function () { m.style.transform = ''; });
    });
  }

  /* ---------- hero embers (canvas) ---------- */
  var cv = d.getElementById('embers');
  if (cv && !reduce && cv.getContext) {
    var ctx = cv.getContext('2d'), W = 0, H = 0, dpr = Math.min(window.devicePixelRatio || 1, 2), ps = [], running = false;
    var N = window.innerWidth < 700 ? 26 : 56;
    function size() {
      var r = cv.getBoundingClientRect(); W = r.width; H = r.height;
      cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }
    function mk(first) {
      return { x: Math.random() * W, y: first ? Math.random() * H : H + 10, r: Math.random() * 2.2 + 0.6, vy: Math.random() * 0.55 + 0.2, sw: Math.random() * 1.2 + 0.3, ph: Math.random() * 6.28, a: Math.random() * 0.6 + 0.25 };
    }
    function init() { size(); ps = []; for (var i = 0; i < N; i++) ps.push(mk(true)); }
    function frame(t) {
      if (!running) return;
      ctx.clearRect(0, 0, W, H);
      for (var i = 0; i < ps.length; i++) {
        var p = ps[i];
        p.y -= p.vy; p.x += Math.sin(t / 900 + p.ph) * 0.35 * p.sw;
        if (p.y < -10) ps[i] = mk(false);
        var fade = Math.min(1, p.y / (H * 0.5));
        ctx.beginPath(); ctx.fillStyle = 'rgba(255,' + Math.round(75 + fade * 60) + ',70,' + (p.a * (0.35 + fade * 0.65)) + ')';
        ctx.shadowColor = '#ff2a3a'; ctx.shadowBlur = 10; ctx.arc(p.x, p.y, p.r, 0, 6.283); ctx.fill();
      }
      requestAnimationFrame(frame);
    }
    init();
    window.addEventListener('resize', init);
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) {
        es.forEach(function (e) { var on = e.isIntersecting; if (on && !running) { running = true; requestAnimationFrame(frame); } else if (!on) running = false; });
      }).observe(cv);
    } else { running = true; requestAnimationFrame(frame); }
  }
})();
