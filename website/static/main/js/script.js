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

// Mobile toggle functionality
function initMobileToggle() {
  const statusCard = document.querySelector('.status-card');
  
  // Check if we're on mobile
  if (window.innerWidth <= 768) {
    // Start collapsed on mobile
    statusCard.classList.add('collapsed');
    
    // Toggle on click
    statusCard.addEventListener('click', function(e) {
      this.classList.toggle('collapsed');
      this.classList.toggle('expanded');
    });
  }
}

// Front Page Opening Hours JS
// Update clinic status based on current time
function updateClinicStatus() {
    // Current time in UTC+5:45 (Nepal Time)
    const now = new Date();
    const day = now.getDay();
    const hour = now.getHours();
    const minutes = now.getMinutes();
    const currentTime = hour + (minutes / 60);
    const statusText = document.getElementById('status-text');
    const statusDot = document.getElementById('status-dot');
    let isOpen = false;
    
    if (day === 6) {
        if (currentTime >= 7 && currentTime < 15) {
            isOpen = true;
        }
    } 

    else {
        if (currentTime >= 7 && currentTime < 19) {
            isOpen = true;
        }
    }

    if (isOpen) {
        statusText.innerText = "OPEN";
        statusText.style.color = "#71C028";
        statusDot.style.backgroundColor = "#71C028";
        statusDot.style.boxShadow = "0 0 0 rgba(113, 192, 40, 0.4)";
        statusDot.style.animation = "statusPulse 2s infinite";
    } else {
        statusText.innerText = "CLOSED";
        statusText.style.color = "#ff4d8d";
        statusDot.style.backgroundColor = "#ff4d8d";
        statusDot.style.animation = "none";
        statusDot.style.boxShadow = "none";
    }
}

document.addEventListener('DOMContentLoaded', function() {
  initMobileToggle();
  updateClinicStatus();
});

window.addEventListener('resize', function() {
  const statusCard = document.querySelector('.status-card');
  if (window.innerWidth <= 768) {
    if (!statusCard.classList.contains('collapsed') && !statusCard.classList.contains('expanded')) {
      statusCard.classList.add('collapsed');
    }
  } else {

    statusCard.classList.remove('collapsed', 'expanded');
  }
});

setInterval(updateClinicStatus, 30000);

