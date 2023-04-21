#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, { json: true }, (err, response, data) => {
  if (err) {
    console.log(err);
    return;
  }
  const completedTasks = {};

  data.forEach(task => {
    if (task.completed === true) {
      if (!completedTasks[task.userId]) {
        completedTasks[task.userId] = 1;
      } else {
        completedTasks[task.userId]++;
      }
    }
  });

  console.log(completedTasks);
});
