#!/usr/bin/node
const req = require('request');
req.get(process.argv[2]).on('request', function (resp) {
    console.log(`code: ${resp.statusCode}`);

});