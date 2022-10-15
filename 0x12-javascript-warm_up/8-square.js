#!/usr/bin/node
const square = parseInt(process.argv[2]);
if (Number.isNaN(size)) {
  console.log('Missing size');
 } else {
 let i = 0;
    while (i < square) {
      s = '';
      i++;
      for (let j = 0; j < size; j++) {
        s += 'X';
      }
      console.log(s);
    }
}
