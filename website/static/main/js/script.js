// Auto-update year
document.getElementById('year').textContent = new Date().getFullYear();

// Theme toggle with persistence
const toggleButton = document.getElementById('theme-toggle');
const themeIcon = document.getElementById('theme-icon');

// Load saved theme on page load
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'dark') {
  document.body.classList.add('dark-mode');
  themeIcon.classList.remove('fa-moon');
  themeIcon.classList.add('fa-sun');
}

toggleButton.addEventListener('click', () => {
  document.body.classList.toggle('dark-mode');

  if (document.body.classList.contains('dark-mode')) {
    themeIcon.classList.remove('fa-moon');
    themeIcon.classList.add('fa-sun');
    localStorage.setItem('theme', 'dark');
  } else {
    themeIcon.classList.remove('fa-sun');
    themeIcon.classList.add('fa-moon');
    localStorage.setItem('theme', 'light');
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

// Testimonial slider
const track = document.getElementById('track');
const nextBtn = document.getElementById('nextBtn');
const prevBtn = document.getElementById('prevBtn');

// Calculate the width of one card + the gap
const cardWidth = document.querySelector('.testimonial-card').offsetWidth + 20;

nextBtn.addEventListener('click', () => {
  // If we reach the end, scroll back to start, otherwise move right
  if (track.scrollLeft + track.offsetWidth >= track.scrollWidth) {
    track.scrollTo({ left: 0, behavior: 'smooth' });
  } else {
    track.scrollBy({ left: cardWidth, behavior: 'smooth' });
  }
});

prevBtn.addEventListener('click', () => {
  // If at the start, scroll to the end, otherwise move left
  if (track.scrollLeft <= 0) {
    track.scrollTo({ left: track.scrollWidth, behavior: 'smooth' });
  } else {
    track.scrollBy({ left: -cardWidth, behavior: 'smooth' });
  }
});