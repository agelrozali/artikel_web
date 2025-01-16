// scripts.js

document.addEventListener('DOMContentLoaded', function() {
    // Example function to toggle a class on an element
    function toggleClass(element, className) {
        if (element.classList.contains(className)) {
            element.classList.remove(className);
        } else {
            element.classList.add(className);
        }
    }

    // Example usage: Toggle 'active' class on a button click
    const button = document.querySelector('#toggleButton');
    if (button) {
        button.addEventListener('click', function() {
            toggleClass(button, 'active');
        });
    }

    // Add more JavaScript functionality as needed
});