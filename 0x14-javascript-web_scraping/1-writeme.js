#!/usr/bin/node

const fs = require("fs")

file_ = process.argv[2]
str_ = process.argv[3]

fs.writeFile(file_,  str_, {encoding: "utf-8"}, (err) => {
	if (err) throw err;
});
