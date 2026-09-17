/* AltaCoco Home — small site script: mobile nav, reveal-on-scroll, contact form. */
(function () {
  // Mobile navigation toggle
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Subtle reveal on scroll
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('is-visible'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('is-visible'); });
  }

  // Editor's Choice category filter (client-side, optional)
  var chips = document.querySelectorAll('[data-filter]');
  var picks = document.querySelectorAll('[data-cats]');
  if (chips.length && picks.length) {
    chips.forEach(function (chip) {
      chip.addEventListener('click', function (ev) {
        ev.preventDefault();
        var f = chip.getAttribute('data-filter');
        chips.forEach(function (c) { c.classList.toggle('is-active', c === chip); });
        picks.forEach(function (p) {
          var cats = p.getAttribute('data-cats').split(',');
          p.hidden = !(f === 'all' || cats.indexOf(f) !== -1);
        });
      });
    });
  }

  // Contact form: no backend wired yet — compose an email instead.
  // Replace this with your form service (Formspree, Netlify Forms, etc.) before launch.
  var form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var data = new FormData(form);
      var lines = [];
      data.forEach(function (v, k) { if (v) lines.push(k + ': ' + v); });
      var subject = 'Project inquiry — ' + (data.get('Project Type') || 'AltaCoco Home');
      var href = 'mailto:cs@altacoco.com?subject=' + encodeURIComponent(subject) +
                 '&body=' + encodeURIComponent(lines.join('\n'));
      var status = document.getElementById('form-status');
      if (status) status.textContent = 'Opening your email app with the details filled in…';
      window.location.href = href;
    });
  }
})();
