#!/usr/bin/node

if ((typeof process.argv[2] === 'undefined') && (typeof process.argv[3] === 'undefined')) {
  console.log('undefined is undefined');
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
