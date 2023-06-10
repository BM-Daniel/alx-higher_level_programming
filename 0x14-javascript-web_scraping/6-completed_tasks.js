#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const complete = {};
    const activities = JSON.parse(body);

    for (const count in activities) {
      const activity = activities[count];
      if (activity.completed === true) {
        if (complete[activity.userId] === undefined) {
          complete[activity.userId] = 1;
        } else {
          complete[activity.userId]++;
        }
      }
    }
    console.log(complete);
  }
});
