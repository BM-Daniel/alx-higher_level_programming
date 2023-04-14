#!/usr/bin/node

const fileSystem = require('fs');
const file1 = fileSystem.readFileSync(process.argv[2]);
const file2 = fileSystem.readFileSync(process.argv[3]);

fileSystem.writeFileSync(process.argv[4], file1 + file2);
