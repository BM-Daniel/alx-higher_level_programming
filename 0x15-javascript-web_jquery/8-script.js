$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (info) {
  $('UL#list_movies').append(...info.results.map(movie => `<li>${movie.title}</li>`));
});
