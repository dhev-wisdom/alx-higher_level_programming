#!/usr/bin/node
exports.esrever = function (list) {
	const len = list.length;
	let new_list = [];
	for (let i = 0; i < len; i++) {
		new_list[len - i - 1] = list[i];
	}

	return (new_list);
}
