#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
request('https://swapi-api.hbtn.io/api/films/' + id, function (err, response, body) {
  if (err) throw err;
  const movie = JSON.parse(body);
  console.log(movie.title);
});
