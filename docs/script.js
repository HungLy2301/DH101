/* ============================================================
   Hung Ly — Portfolio interactions
   - Theme toggle (light/dark) with persistence
   - Mobile menu
   - Project filtering & search (journey page)
   - Smooth scroll reveal
   ============================================================ */

(function () {
  'use strict';

  // ── Theme toggle ─────────────────────────────────────────
  const themeToggle = document.querySelector('.theme-toggle');
  const html = document.documentElement;
  const savedTheme = localStorage.getItem('theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const initialTheme = savedTheme || (prefersDark ? 'dark' : 'light');
  html.setAttribute('data-theme', initialTheme);
  updateThemeIcon(initialTheme);

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const current = html.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
      updateThemeIcon(next);
    });
  }

  function updateThemeIcon(theme) {
    if (themeToggle) {
      themeToggle.textContent = theme === 'dark' ? '☀' : '☾';
      themeToggle.setAttribute('aria-label',
        theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
    }
  }

  // ── Mobile menu ──────────────────────────────────────────
  const menuBtn = document.querySelector('.menu-btn');
  const navLinks = document.querySelector('.nav-links');
  if (menuBtn && navLinks) {
    menuBtn.addEventListener('click', () => {
      const isOpen = navLinks.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', isOpen);
      menuBtn.textContent = isOpen ? '✕' : '☰';
    });
    // Close menu when a link is clicked
    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('open');
        menuBtn.setAttribute('aria-expanded', 'false');
        menuBtn.textContent = '☰';
      });
    });
  }

  // ── Filter + Search (Journey page) ───────────────────────
  const filterBtns = document.querySelectorAll('.filter-btn');
  const searchBox = document.getElementById('search-box');
  const cards = document.querySelectorAll('.project-card');
  const noResults = document.getElementById('no-results');

  let activeFilter = 'all';
  let activeQuery = '';

  function applyFilters() {
    let visibleCount = 0;
    cards.forEach(card => {
      const tag = (card.dataset.tag || '').toLowerCase();
      const text = card.textContent.toLowerCase();
      const matchesFilter = activeFilter === 'all' || tag === activeFilter.toLowerCase();
      const matchesSearch = !activeQuery || text.includes(activeQuery);
      const visible = matchesFilter && matchesSearch;
      card.style.display = visible ? '' : 'none';
      if (visible) visibleCount++;
    });
    if (noResults) noResults.style.display = visibleCount === 0 ? 'block' : 'none';
  }

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeFilter = btn.dataset.filter;
      applyFilters();
    });
  });

  if (searchBox) {
    searchBox.addEventListener('input', e => {
      activeQuery = e.target.value.trim().toLowerCase();
      applyFilters();
    });
  }

  // ── Fade-in on scroll ────────────────────────────────────
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('fade-up');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

    document.querySelectorAll('.nav-card, .project-card, .section-header').forEach(el => {
      observer.observe(el);
    });
  }
})();