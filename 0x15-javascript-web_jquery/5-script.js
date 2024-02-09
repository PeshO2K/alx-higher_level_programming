// script.js
$(document).ready(function() {
    // Wait for the DOM to be ready

    // Handle the click event on DIV#add_item
    $('#add_item').click(function() {
      // Append a new <li> element to the <ul> with class 'my_list'
      $('<li>Item</li>').appendTo('ul.my_list');
    });
  });
