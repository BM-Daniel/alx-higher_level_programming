$('document').ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (info) {
    $('DIV#hello').text(info.hello);
  });
});