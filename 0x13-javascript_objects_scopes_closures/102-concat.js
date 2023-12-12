#!/usr/bin/node
const fs = require('fs');
const path1 = process.argv[2];
const path2 = process.argv[3];
const destination = process.argv[4];

fs.readFile(path1, 'utf8', (err, data1) => {
  if (err) throw err;
  fs.readFile(path2, 'utf8', (err, data2) => {
    if (err) throw err;
    fs.writeFile(destination, data1 + data2, (err) => {
      if (err) throw err;
    });
  });
});
