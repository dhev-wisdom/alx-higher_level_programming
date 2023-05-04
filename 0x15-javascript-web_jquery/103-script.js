/* global $ */
$(document).ready(function () {
  const fetchTranslation = () => {
    const langCode = $('#language_code').val;
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + langCode;
    $.get(url, function (data, textStatus) {
      $('#hello').text(data.hello);
    });
  };
  $('#btn_translate').click(function () {
    fetchTranslation();
  });
  $('#language_code').keypress(function () {
    if (event.keyCode === 13) fetchTranslation();
  });
});
