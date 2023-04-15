#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }

    Rectangle.prototype.print = function () {
      for (let height = 0; height < h; height++) {
        let printRectangle = '';
        for (let width = 0; width < w; width++) {
          printRectangle += 'X';
        }
        console.log(printRectangle);
      }
    };
  }
};
