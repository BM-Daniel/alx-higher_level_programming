#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const result = JSON.parse(body).results;
    let count = 0;

    for (const resultIndex in result) {
      const resultCharacters = result[resultIndex].characters;

      for (const charactersIndex in resultCharacters) {
        if (resultCharacters[charactersIndex].includes('18')) count++;
      }
    }

    console.log(count);
  }
});
