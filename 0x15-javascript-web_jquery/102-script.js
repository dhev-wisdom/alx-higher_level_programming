/* global $ */
$(document).ready(function () {
  const langCode = $('input#language_code').val;
  $('#btn_translate').click(function () {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + langCode;
    $.get(url, function (data, textStatus) {
      $('#hello').text(data.hello);
    });
  });
});
