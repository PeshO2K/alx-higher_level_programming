// script.js
$(document).ready(function() {
    // Wait for the DOM to be ready

    // Handle click event on DIV#add_item
    $('#add_item').click(function() {
      // Add a new <li> element to the list
      $('<li>Item</li>').appendTo('ul.my_list');
    });

    // Handle click event on DIV#remove_item
    $('#remove_item').click(function() {
      // Remove the last <li> element from the list
      $('ul.my_list li:last-child').remove();
    });

    // Handle click event on DIV#clear_list
    $('#clear_list').click(function() {
      // Remove all <li> elements from the list
      $('ul.my_list').empty();
    });
  });
