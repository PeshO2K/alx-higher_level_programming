// script.js
$(document).ready(function() {
    // Wait for the DOM to be ready

    // Handle the click event on DIV#update_header
    $('#update_header').click(function() {
      // Update the text of the <header> element to "New Header!!!"
      $('header').text('New Header!!!');
    });
  });
