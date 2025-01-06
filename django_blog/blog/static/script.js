// blog/static/script.js
document.addEventListener('DOMContentLoaded', function() {
    console.log('JavaScript is loaded and ready to go!');

    // Example: Add a simple form validation
    const loginForm = document.querySelector('form');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            const username = document.querySelector('input[name="username"]').value;
            const password = document.querySelector('input[name="password"]').value;

            if (!username || !password) {
                event.preventDefault(); // Prevent form submission
                alert('Please fill in both fields.');
            }
        });
    }
});