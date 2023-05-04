/* global $ */
$(document).ready(() => {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
    $.each(data.results, function (index, value) {
      $('#list_movies').append('<li>' + value.title + '</li>');
    });
  });
});
