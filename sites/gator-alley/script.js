(function () {
  var root = document.documentElement;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var $ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* hero orchestrated load */
  var hero = document.querySelector('.hero, .phero');
  if (hero) { window.addEventListener('load', function () { requestAnimationFrame(function () { hero.classList.add('go'); }); }); setTimeout(function () { hero.classList.add('go'); }, 900); }

  /* scroll: progress, header, parallax, method line */
  var hdr = document.querySelector('.header'), bar = document.querySelector('.progress i'), last = 0, tick = false;
  var par = $('[data-speed]'), steps = document.querySelector('.steps');
  function frame() {
    var y = window.scrollY, h = root.scrollHeight - innerHeight;
    if (bar) bar.style.transform = 'scaleX(' + (h > 0 ? y / h : 0) + ')';
    if (hdr) { hdr.classList.toggle('shrink', y > 30); hdr.classList.toggle('hide', y > last + 4 && y > 400 && !root.classList.contains('menu-open')); if (y < last - 4) hdr.classList.remove('hide'); }
    last = y;
    if (!reduce && innerWidth > 1000) par.forEach(function (el) {
      var r = el.getBoundingClientRect(); if (r.bottom < -100 || r.top > innerHeight + 100) return;
      el.style.translate = '0 ' + (((r.top + r.height / 2) - innerHeight / 2) * -parseFloat(el.dataset.speed)).toFixed(1) + 'px';
    });
    if (steps) {
      var r2 = steps.getBoundingClientRect(), p = Math.min(1, Math.max(0, (innerHeight * .62 - r2.top) / r2.height));
      steps.style.setProperty('--lp', p.toFixed(3));
      $('.step', steps).forEach(function (s) { s.classList.toggle('on', s.getBoundingClientRect().top < innerHeight * .62); });
    }
    tick = false;
  }
  addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(frame); } }, { passive: true });
  addEventListener('resize', frame); frame();

  /* reveals */
  var io = 'IntersectionObserver' in window ? new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: .15, rootMargin: '0px 0px -6% 0px' }) : null;
  $('.rv').forEach(function (el, i) { if (io) { el.style.transitionDelay = (el.dataset.d || 0) + 'ms'; io.observe(el); } else el.classList.add('in'); });

  /* count-up */
  var cio = 'IntersectionObserver' in window ? new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (!e.isIntersecting) return; cio.unobserve(e.target);
      var el = e.target, end = parseFloat(el.dataset.count), dec = +el.dataset.dec || 0, t0 = null;
      (function step(t) { t0 = t0 || t; var k = Math.min(1, (t - t0) / 1500); el.textContent = (end * (1 - Math.pow(1 - k, 3))).toFixed(dec); if (k < 1) requestAnimationFrame(step); })(performance.now());
    });
  }, { threshold: .7 }) : null;
  if (cio && !reduce) $('[data-count]').forEach(function (el) { el.textContent = '0'; cio.observe(el); });

  /* menu */
  var mb = document.querySelector('.menu-btn');
  if (mb) {
    mb.addEventListener('click', function () { var o = root.classList.toggle('menu-open'); mb.setAttribute('aria-expanded', o); });
    $('.drawer a').forEach(function (a) { a.addEventListener('click', function () { root.classList.remove('menu-open'); mb.setAttribute('aria-expanded', false); }); });
  }

  /* faq: smooth open/close */
  $('details').forEach(function (d) {
    var s = d.querySelector('summary'), a = d.querySelector('.ans');
    s.addEventListener('click', function (e) {
      if (reduce) return; e.preventDefault();
      if (d.open) { a.style.height = a.offsetHeight + 'px'; requestAnimationFrame(function () { a.style.transition = 'height .4s cubic-bezier(.2,.8,.2,1)'; a.style.height = '0px'; }); setTimeout(function () { d.open = false; a.style.height = ''; a.style.transition = ''; }, 400); }
      else { d.open = true; var h = a.scrollHeight; a.style.height = '0px'; requestAnimationFrame(function () { a.style.transition = 'height .45s cubic-bezier(.2,.8,.2,1)'; a.style.height = h + 'px'; }); setTimeout(function () { a.style.height = ''; a.style.transition = ''; }, 460); }
    });
  });

  if (fine && !reduce) {
    /* floating photo that follows the cursor over program rows */
    var rows = $('.prow[data-img]'), peek = document.querySelector('.peek');
    if (peek && rows.length) {
      var pi = peek.querySelector('img'), tx = 0, ty = 0, cx = 0, cy = 0, run = false;
      function loop() { cx += (tx - cx) * .14; cy += (ty - cy) * .14; peek.style.transform = 'translate(' + cx.toFixed(1) + 'px,' + cy.toFixed(1) + 'px) rotate(' + (((tx - cx) * .04)).toFixed(2) + 'deg)'; if (run) requestAnimationFrame(loop); }
      rows.forEach(function (r) {
        r.addEventListener('mouseenter', function () { pi.src = r.dataset.img; peek.style.aspectRatio = r.dataset.ar; run = true; peek.classList.add('on'); requestAnimationFrame(loop); });
        r.addEventListener('mousemove', function (e) { tx = e.clientX + 28; ty = e.clientY - 120; if (!peek.classList.contains('on')) { cx = tx; cy = ty; } });
        r.addEventListener('mouseleave', function () { peek.classList.remove('on'); run = false; });
      });
    }
    /* 3D tilt + light on cards */
    $('.pcard,.hero-card').forEach(function (c) {
      c.addEventListener('mousemove', function (e) {
        var r = c.getBoundingClientRect(), x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
        c.style.setProperty('--mx', (x * 100) + '%'); c.style.setProperty('--my', (y * 100) + '%');
        c.style.transform = 'perspective(900px) rotateX(' + ((.5 - y) * 7).toFixed(2) + 'deg) rotateY(' + ((x - .5) * 9).toFixed(2) + 'deg) translateY(-6px)';
      });
      c.addEventListener('mouseleave', function () { c.style.transform = ''; });
    });
    /* magnetic buttons */
    $('.btn').forEach(function (b) {
      b.addEventListener('mousemove', function (e) { var r = b.getBoundingClientRect(); b.style.transform = 'translate(' + ((e.clientX - r.left - r.width / 2) * .12).toFixed(1) + 'px,' + ((e.clientY - r.top - r.height / 2) * .22).toFixed(1) + 'px)'; });
      b.addEventListener('mouseleave', function () { b.style.transform = ''; });
    });
    /* hero stage depth */
    var st = document.querySelector('.stage');
    if (st) {
      var sun = st.querySelector('.sun-in'), arch = st.querySelector('.arch');
      st.addEventListener('mousemove', function (e) {
        var r = st.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
        if (sun) sun.style.transform = 'translate(' + (x * -26).toFixed(1) + 'px,' + (y * -20).toFixed(1) + 'px)';
        if (arch) arch.style.transform = 'translate(' + (x * 12).toFixed(1) + 'px,' + (y * 8).toFixed(1) + 'px)';
      });
      st.addEventListener('mouseleave', function () { if (sun) sun.style.transform = ''; if (arch) arch.style.transform = ''; });
    }
  }

  /* lead form */
  $('form[data-form]').forEach(function (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var msg = form.querySelector('.form-msg'), btn = form.querySelector('button');
      btn.disabled = true; msg.textContent = 'Sending your request…';
      fetch(form.action, { method: 'POST', headers: { Accept: 'application/json' }, body: new FormData(form) })
        .then(function (r) { if (!r.ok) throw 0; return r.json(); })
        .then(function () { form.reset(); msg.textContent = 'Request sent. Jacob will follow up with you shortly.'; btn.disabled = false; })
        .catch(function () { msg.innerHTML = 'The request did not send. Call <a href="tel:+19418420849">(941) 842-0849</a> or try again.'; btn.disabled = false; });
    });
  });
})();
