$(document).ready(function() {
    function fetchTranslation() {
      const languageCode = $('#language_code').val();
      const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=' + languageCode;

      $.get(apiUrl, function(data) {
        $('#hello').text(data.hello);
      });
    }

    $('#btn_translate').click(fetchTranslation);

    $('#language_code').keypress(function(event) {
      if (event.which === 13) { // Check if the pressed key is ENTER (key code 13)
        fetchTranslation();
      }
    });
  });
