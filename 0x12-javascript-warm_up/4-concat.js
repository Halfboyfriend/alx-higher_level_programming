#!/usr/bin/node
console.log(typeof process.argv[2] === 'undefined' + ' is ' + process.argv[2] ? 'No argument' : process.argv[2] + ' is ' + process.argv[3]);