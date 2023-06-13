$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (info) {
  $('DIV#character').text(info.name);
});
