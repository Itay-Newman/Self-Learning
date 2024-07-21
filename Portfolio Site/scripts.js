// Toggle navigation menu for small screens
function toggleMenu() {
    const nav = document.querySelector('header nav ul');
    nav.classList.toggle('active');
}

// Form validation
function validateForm(event) {
    event.preventDefault(); // Prevent form submission

    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();
    let valid = true;

    // Clear previous error messages
    document.querySelectorAll('.error').forEach(el => el.remove());

    if (!name) {
        showError('name', 'Name is required.');
        valid = false;
    }
    if (!email || !validateEmail(email)) {
        showError('email', 'Valid email is required.');
        valid = false;
    }
    if (!message) {
        showError('message', 'Message is required.');
        valid = false;
    }

    if (valid) {
        // Submit the form (here we just display a success message for demonstration)
        alert('Form submitted successfully!');
    }
}

function showError(fieldId, message) {
    const field = document.getElementById(fieldId);
    const error = document.createElement('div');
    error.className = 'error';
    error.textContent = message;
    field.parentElement.appendChild(error);
}

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

// Typewriter effect for header
const typewriterText = "Welcome to My Portfolio";
let index = 0;

function typewriter() {
    if (index < typewriterText.length) {
        document.querySelector('header h1').textContent += typewriterText.charAt(index);
        index++;
        setTimeout(typewriter, 150);
    }
}

// Smooth scrolling for navigation links
document.querySelectorAll('nav ul li a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('.menu-toggle').addEventListener('click', toggleMenu);
    document.querySelector('form').addEventListener('submit', validateForm);
    typewriter();
});
