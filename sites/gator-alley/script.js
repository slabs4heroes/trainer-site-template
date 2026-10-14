(function () {
  var root = document.documentElement;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* hero load-in */
  var hero = document.querySelector('.hero, .phero');
  if (hero) { window.addEventListener('load', function () { requestAnimationFrame(function () { hero.classList.add('go'); }); }); setTimeout(function () { hero.classList.add('go'); }, 900); }

  /* scroll: progress bar, header, method line */
  var hdr = document.querySelector('.header'), bar = document.querySelector('.progress i'), last = 0, tick = false;
  var steps = document.querySelector('.steps');
  function frame() {
    var y = window.scrollY, h = root.scrollHeight - innerHeight;
    if (bar) bar.style.transform = 'scaleX(' + (h > 0 ? y / h : 0) + ')';
    if (hdr) {
      hdr.classList.toggle('shrink', y > 30);
      hdr.classList.toggle('hide', y > last + 4 && y > 400 && !root.classList.contains('menu-open'));
      if (y < last - 4) hdr.classList.remove('hide');
    }
    last = y;
    if (steps) {
      var r = steps.getBoundingClientRect(), p = Math.min(1, Math.max(0, (innerHeight * .62 - r.top) / r.height));
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
  $('.rv').forEach(function (el) { if (io) { el.style.transitionDelay = (el.dataset.d || 0) + 'ms'; io.observe(el); } else el.classList.add('in'); });

  /* mobile menu */
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
