/* global $ */
$(document).ready(function () {
  $('div#toggle_header').click(function () {
    $('header').toggleClass(function () {
      if ($(this).hasClass('green')) {
        $(this).removeClass('green').addClass('red');
      } else if ($(this).hasClass('red')) {
        $(this).removeClass('red').addClass('green');
      }
    });
  });
});
