#!/usr/bin/node
const Squares = require('./5-square.js');
class Square extends Squares {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    if (this.width) {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
