// script.js
document.addEventListener('DOMContentLoaded', function () {
    // Wait for the DOM content to be fully loaded

    // Select the <header> element and update its text color to red
    const headerElement = document.querySelector('header');
    if (headerElement) {
      headerElement.style.color = '#FF0000';
    } else {
      console.error('Header element not found');
    }
  });
