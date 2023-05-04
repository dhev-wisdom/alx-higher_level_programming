/* global $ */
$(document).ready(function () {
  $('#add_item').click(function () {
    $(this).find('ul#my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(function () {
    $(this).find('ul#my_list').find('li:last').remove();
  });
  $('#clear_list').click(function () {
    $(this).find('my_list').empty();
  });
});
