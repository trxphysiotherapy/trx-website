// Auto-update year
document.getElementById('year').textContent = new Date().getFullYear();

// Theme toggle
const toggleButton = document.getElementById('theme-toggle');
const themeIcon = document.getElementById('theme-icon');

toggleButton.addEventListener('click', () => {
  document.body.classList.toggle('dark-mode');

  if (document.body.classList.contains('dark-mode')) {
    themeIcon.classList.remove('fas', 'fa-moon');
    themeIcon.classList.add('fas', 'fa-sun');
  } else {
    themeIcon.classList.remove('fas', 'fa-sun');
    themeIcon.classList.add('fas', 'fa-moon');
  }
});

// Mobile menu toggle
const menuToggle = document.getElementById('menu-toggle');
const navLinks = document.getElementById('nav-links');
const navActions = document.querySelector('.nav-actions');

menuToggle.addEventListener('click', () => {
  navLinks.classList.toggle('active');
  navActions.classList.toggle('active');
});