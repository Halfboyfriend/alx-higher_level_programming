#!/usr/bin/node
const request = require('request');
let link = 'http://swapi.co/api/films/' + process.argv[2];
request(link, function (error, response, body){
    console.log(error || JSON.parse(body).title);
});
