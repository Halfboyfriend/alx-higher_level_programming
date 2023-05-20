#!/usr/bin/node
const pat = require('fs');
const request = require('request');
request(process.argv[2]).pipe(pat.createWriteStream(process.argv[3]));