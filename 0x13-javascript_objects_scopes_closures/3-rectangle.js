#!/usr/bin/node
module.exports = class Rectangle {
	constructor (w, h) {
		if (w > 0 && h > 0)
		{
			this.width = w;
			this.height = h;
		}
	}

	print() {
		const x = this.width;
		const y = this.height;
		for (let a = 0; a < y; a++) {
			let arr = [];
			for (let b = 0; b < x; b++) {
			arr.push('X');
			}
			console.log(arr.join(''));
		}
	}
}
