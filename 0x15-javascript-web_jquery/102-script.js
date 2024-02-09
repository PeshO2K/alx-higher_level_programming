$(document).ready(function() {
    $('INPUT#btn_translate').click(function() {
      const languageCode = $('INPUT#language_code').val();
      const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=${languageCode}';

      $.getJSON(apiUrl, function(data) {
        $('DIV#hello').text(data.hello);
      });
    });
  });
// $(document).ready(function () {
//     $('INPUT#btn_translate').click(function () {
//       const lan = $('INPUT#language_code').val();
//       $.getJSON(`https://hellosalut.stefanbohacek.dev/?lang=${lan}`, function (data) {
//         $('DIV#hello').text(data.hello);
//       });
//     });
//   });
