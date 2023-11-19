#!/usr/bin/node
/**
 * Square class that inherits from previous square class
 */
const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  charPrint (c) {
    const myChar = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let count = '';
      let y = 0;
      while (y < this.width) {
        count += myChar;
        y++;
      }

      console.log(count);
    }
  }
}

module.exports = Square;
