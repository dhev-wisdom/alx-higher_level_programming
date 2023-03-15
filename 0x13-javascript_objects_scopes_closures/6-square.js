#!/usr/bin/node
const Square_ = require('./5-square');

class Square extends Square_ {
	charPrint(c) {
		let _p = '';
		c ? _p = c : _p = 'X';
		const x = this.width;
		const y = this.height;
		for (let a = 0; a < y; a++) {
			let arr = [];
			for (let b = 0; b < x; b++) {
				arr.push(_p);
			}
			console.log(arr.join(''));
		}
	}
}

module.exports = Square;
