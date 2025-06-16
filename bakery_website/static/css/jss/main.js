// static/js/main.js

window.addEventListener('DOMContentLoaded', (event) => {
    // Check if the element exists to avoid errors on other pages
    const newsletterModal = document.getElementById('newsletterModal');
    if (newsletterModal) {
        const closeButton = document.querySelector('.close-button');

        // Show the modal as soon as the home page loads
        newsletterModal.style.display = 'block';

        // When the user clicks on <span> (x), close the modal
        closeButton.onclick = function() {
            newsletterModal.style.display = 'none';
        }

        // When the user clicks anywhere outside of the modal, close it
        window.onclick = function(event) {
            if (event.target == newsletterModal) {
                newsletterModal.style.display = 'none';
            }
        }
    }
});