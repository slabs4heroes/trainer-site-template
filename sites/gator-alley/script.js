(function () {
  var hdr = document.querySelector('.header');
  function onScroll() { if (hdr) hdr.classList.toggle('shrink', window.scrollY > 40); }
  onScroll(); window.addEventListener('scroll', onScroll, { passive: true });

  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    els.forEach(function (el, i) { el.style.transitionDelay = ((i % 3) * 80) + 'ms'; io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add('in'); }); }

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
