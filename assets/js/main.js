/* Meridian demo — nav, project filters, gallery + lightbox, scroll reveal.
   No dependencies. ~4 KB. */
(function () {
  'use strict';

  /* ----- mobile nav ----- */
  var burger = document.querySelector('.burger');
  var nav = document.getElementById('primary-nav');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      var open = burger.getAttribute('aria-expanded') === 'true';
      burger.setAttribute('aria-expanded', String(!open));
      nav.setAttribute('data-open', String(!open));
    });
  }

  /* ----- project filters ----- */
  var filterBar = document.querySelector('[data-filters]');
  if (filterBar) {
    var cards = Array.prototype.slice.call(document.querySelectorAll('[data-sector]'));
    var empty = document.querySelector('[data-empty]');
    filterBar.addEventListener('click', function (e) {
      var btn = e.target.closest('button[data-filter]');
      if (!btn) return;
      var want = btn.getAttribute('data-filter');
      filterBar.querySelectorAll('button').forEach(function (b) {
        b.setAttribute('aria-pressed', String(b === btn));
      });
      var shown = 0;
      cards.forEach(function (c) {
        var hit = want === 'all' || c.getAttribute('data-sector') === want;
        c.hidden = !hit;
        if (hit) shown++;
      });
      if (empty) empty.hidden = shown !== 0;
    });
  }

  /* ----- gallery + lightbox ----- */
  var gal = document.querySelector('[data-gallery]');
  var lb = document.getElementById('lightbox');

  if (gal && lb) {
    var slides = JSON.parse(gal.getAttribute('data-gallery'));
    var stageImg = gal.querySelector('[data-stage-img]');
    var thumbs = Array.prototype.slice.call(gal.querySelectorAll('[data-thumb]'));
    var idx = 0;

    var lbImg = lb.querySelector('[data-lb-img]');
    var lbCap = lb.querySelector('[data-lb-cap]');
    var lbPos = lb.querySelector('[data-lb-pos]');
    var lastFocus = null;

    function paintStage(i) {
      idx = (i + slides.length) % slides.length;
      var s = slides[idx];
      stageImg.src = s.full;
      stageImg.alt = s.alt;
      thumbs.forEach(function (t, n) { t.setAttribute('aria-current', String(n === idx)); });
    }

    function paintLb() {
      var s = slides[idx];
      lbImg.src = s.full;
      lbImg.alt = s.alt;
      lbCap.innerHTML = '<b>' + s.title + '</b>' + s.caption;
      lbPos.textContent = (idx + 1) + ' / ' + slides.length;
    }

    function openLb() {
      lastFocus = document.activeElement;
      paintLb();
      lb.setAttribute('data-open', 'true');
      document.body.setAttribute('data-lb', 'open');
      lb.querySelector('.lb__close').focus();
    }

    function closeLb() {
      lb.removeAttribute('data-open');
      document.body.removeAttribute('data-lb');
      if (lastFocus) lastFocus.focus();
    }

    function step(delta) {
      paintStage(idx + delta);
      if (lb.getAttribute('data-open') === 'true') paintLb();
    }

    thumbs.forEach(function (t, n) {
      t.addEventListener('click', function () { paintStage(n); });
    });

    gal.querySelectorAll('[data-step]').forEach(function (b) {
      b.addEventListener('click', function (e) {
        e.stopPropagation();
        step(parseInt(b.getAttribute('data-step'), 10));
      });
    });

    gal.querySelector('[data-open-lb]').addEventListener('click', openLb);

    lb.querySelectorAll('[data-lb-step]').forEach(function (b) {
      b.addEventListener('click', function () { step(parseInt(b.getAttribute('data-lb-step'), 10)); });
    });
    lb.querySelector('.lb__close').addEventListener('click', closeLb);
    lb.querySelector('.lb__stage').addEventListener('click', function (e) {
      if (e.target === e.currentTarget) closeLb();
    });

    document.addEventListener('keydown', function (e) {
      var open = lb.getAttribute('data-open') === 'true';
      if (!open) return;
      if (e.key === 'Escape') closeLb();
      else if (e.key === 'ArrowRight') step(1);
      else if (e.key === 'ArrowLeft') step(-1);
      else if (e.key === 'Tab') {
        // keep focus inside the lightbox
        var f = lb.querySelectorAll('button');
        var first = f[0], last = f[f.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });

    /* swipe */
    [gal.querySelector('.gal__stage'), lb.querySelector('.lb__stage')].forEach(function (el) {
      if (!el) return;
      var x0 = null, y0 = null;
      el.addEventListener('touchstart', function (e) {
        x0 = e.changedTouches[0].clientX; y0 = e.changedTouches[0].clientY;
      }, { passive: true });
      el.addEventListener('touchend', function (e) {
        if (x0 === null) return;
        var dx = e.changedTouches[0].clientX - x0;
        var dy = e.changedTouches[0].clientY - y0;
        if (Math.abs(dx) > 45 && Math.abs(dx) > Math.abs(dy)) step(dx < 0 ? 1 : -1);
        x0 = null;
      }, { passive: true });
    });

    /* preload neighbours once idle */
    if ('requestIdleCallback' in window) {
      requestIdleCallback(function () {
        slides.forEach(function (s) { var i = new Image(); i.src = s.full; });
      });
    }

    paintStage(0);
  }

  /* ----- scroll reveal ----- */
  var rv = document.querySelectorAll('.rv');
  if (rv.length && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: .08 });
    rv.forEach(function (el) { io.observe(el); });
  } else {
    rv.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* ----- demo contact form ----- */
  var form = document.querySelector('[data-demo-form]');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var out = form.querySelector('[data-form-msg]');
      out.hidden = false;
      out.textContent = 'Thanks — this is the design demo, so nothing was sent. On the live site this posts straight to your inbox.';
    });
  }
})();
