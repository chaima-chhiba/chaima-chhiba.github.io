(function () {
  var d = document;
  var b = d.querySelector('.burger');
  var n = d.querySelector('.nav nav');

  if (!b || !n) return;

  b.addEventListener('click', function () {
    var open = n.classList.toggle('open');
    b.setAttribute('aria-expanded', open);
    b.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  });

  d.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && n.classList.contains('open')) {
      n.classList.remove('open');
      b.setAttribute('aria-expanded', 'false');
      b.setAttribute('aria-label', 'Open menu');
      b.focus();
    }
  });

  n.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') {
      n.classList.remove('open');
      b.setAttribute('aria-expanded', 'false');
      b.setAttribute('aria-label', 'Open menu');
    }
  });
})();
