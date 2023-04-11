#!/usr/bin/node

function fact (n) {
  return ((n === 0 || isNaN(n))
    ? 1
    : fact(n - 1) * n);
}

console.log(fact(Number(process.argv[2])));
