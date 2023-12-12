#!/usr/bin/node
const arg1 = process.argv[2];
const num = Number(arg1);

if (Number.isInteger(num)) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
