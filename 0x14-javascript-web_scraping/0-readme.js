#!/usr/bin/node

const fs = require("fs")

file_ = process.argv[2]

fs.readFile(file_, "utf-8", (err, data) => {
	if (err) console.error(err);
	else if (data) console.log(data);
});
