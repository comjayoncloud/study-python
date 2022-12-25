const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toNumber().trim();

console.log(input - 543);
