(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hdr = document.querySelector('.header'), bar = document.querySelector('.progress i');
  var lastY = 0, ticking = false;

  /* split headings into animated words */
  document.querySelectorAll('[data-split]').forEach(function (el, n) {
    var i = 0;
    (function walk(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (c) {
        if (c.nodeType === 3) {
          var frag = document.createDocumentFragment();
          c.textContent.split(/(\s+)/).forEach(function (t) {
            if (!t) return;
            if (/^\s+$/.test(t)) { frag.appendChild(document.createTextNode(' ')); return; }
            var w = document.createElement('span'); w.className = 'w';
            var s = document.createElement('span'); s.textContent = t; s.style.setProperty('--i', i++);
            w.style.setProperty('--i', i); w.appendChild(s); frag.appendChild(w);
          });
          node.replaceChild(frag, c);
        } else if (c.nodeType === 1) walk(c);
      });
    })(el);
    if (n === 0 || reduce) requestAnimationFrame(function () { el.classList.add('go'); });
  });
  var sio = 'IntersectionObserver' in window ? new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('go'); sio.unobserve(e.target); } });
  }, { threshold: 0.3 }) : null;
  document.querySelectorAll('[data-split]:not(.go)').forEach(function (el) { sio ? sio.observe(el) : el.classList.add('go'); });

  /* scroll: progress bar, header hide/show, parallax, path line */
  var photos = document.querySelectorAll('.hero-photo'), line = document.querySelector('[data-line]');
  function onScroll() {
    var y = window.scrollY, h = document.documentElement.scrollHeight - window.innerHeight;
    if (bar) bar.style.transform = 'scaleX(' + (h > 0 ? y / h : 0) + ')';
    if (hdr) { hdr.classList.toggle('shrink', y > 40); hdr.classList.toggle('hide', y > lastY && y > 320); }
    lastY = y;
    if (!reduce && window.innerWidth > 980) photos.forEach(function (p, i) { p.style.translate = '0 ' + (y * (i ? -0.05 : 0.07)).toFixed(1) + 'px'; });
    if (line) { var r = line.getBoundingClientRect(), p = Math.min(1, Math.max(0, (window.innerHeight * 0.7 - r.top) / r.height)); line.style.setProperty('--lp', p.toFixed(3)); }
    ticking = false;
  }
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();

  /* reveal on scroll */
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }); }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
    els.forEach(function (el, i) { el.style.transitionDelay = ((i % 3) * 90) + 'ms'; io.observe(el); });
  } else els.forEach(function (el) { el.classList.add('in'); });

  /* count-up stats */
  var cio = 'IntersectionObserver' in window ? new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (!e.isIntersecting) return; cio.unobserve(e.target);
      var el = e.target, end = parseFloat(el.dataset.count), dec = +el.dataset.dec || 0, suf = el.dataset.suffix || '', t0 = null;
      if (reduce) return;
      (function step(t) { t0 = t0 || t; var k = Math.min(1, (t - t0) / 1400), v = end * (1 - Math.pow(1 - k, 3)); el.textContent = v.toFixed(dec) + suf; if (k < 1) requestAnimationFrame(step); })(performance.now());
    });
  }, { threshold: 0.6 }) : null;
  document.querySelectorAll('[data-count]').forEach(function (el) { if (cio && !reduce) { el.textContent = '0' + (el.dataset.suffix || ''); cio.observe(el); } });

  if (!reduce && window.matchMedia('(hover: hover)').matches) {
    /* spotlight + 3D tilt on program cards */
    document.querySelectorAll('.pcard').forEach(function (c) {
      c.addEventListener('mousemove', function (e) {
        var r = c.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top;
        c.style.setProperty('--mx', x + 'px'); c.style.setProperty('--my', y + 'px');
        c.style.transform = 'translateY(-10px) perspective(900px) rotateX(' + ((y / r.height - .5) * -6).toFixed(2) + 'deg) rotateY(' + ((x / r.width - .5) * 6).toFixed(2) + 'deg)';
      });
      c.addEventListener('mouseleave', function () { c.style.transform = ''; });
    });
    /* magnetic buttons */
    document.querySelectorAll('.primary,.small-cta').forEach(function (b) {
      b.addEventListener('mousemove', function (e) { var r = b.getBoundingClientRect(); b.style.transform = 'translate(' + ((e.clientX - r.left - r.width / 2) * .18).toFixed(1) + 'px,' + ((e.clientY - r.top - r.height / 2) * .28 - 3).toFixed(1) + 'px)'; });
      b.addEventListener('mouseleave', function () { b.style.transform = ''; });
    });
    /* hero mouse depth */
    var art = document.querySelector('[data-tilt]');
    if (art) {
      art.addEventListener('mousemove', function (e) { var r = art.getBoundingClientRect(); art.style.setProperty('--rx', (((e.clientY - r.top) / r.height - .5) * -5).toFixed(2) + 'deg'); art.style.setProperty('--ry', (((e.clientX - r.left) / r.width - .5) * 6).toFixed(2) + 'deg'); art.style.transform = 'rotateX(var(--rx)) rotateY(var(--ry))'; });
      art.addEventListener('mouseleave', function () { art.style.transform = ''; });
    }
  }

  /* lead form */
  document.querySelectorAll('form[data-form]').forEach(function (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var msg = form.querySelector('.form-msg'), btn = form.querySelector('button');
      btn.disabled = true; msg.textContent = 'Sending…';
      fetch(form.action, { method: 'POST', headers: { Accept: 'application/json' }, body: new FormData(form) })
        .then(function (r) { if (!r.ok) throw new Error(); return r.json(); })
        .then(function () { form.reset(); msg.textContent = 'Thank you — Jacob will follow up with you shortly.'; btn.disabled = false; })
        .catch(function () { msg.innerHTML = 'Something went wrong. Please call <a href="tel:+19418420849">(941) 842-0849</a>.'; btn.disabled = false; });
    });
  });
})();
