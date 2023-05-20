#!/usr/bin/node
const { error } = require('console');
const pt = require('fs');
pt.writeFile(process.argv[2], process.argv[3], error => {
    if (error) {
        console.log(error);
    };
});
