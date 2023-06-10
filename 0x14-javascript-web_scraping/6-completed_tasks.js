#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const complete = {};
    const work = JSON.parse(body);

    for (const count in work) {
      const temp = work[count];

      if (temp.completed === true) {
        if (complete[temp.userId] === undefined) {
          complete[temp.userId] = 1;
        } else {
          complete[temp.userId]++;
        }
      }
    }

    console.log(complete);
  }
});
