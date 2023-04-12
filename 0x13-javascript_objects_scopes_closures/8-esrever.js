#!/usr/bin/node

exports.esrever = function (list) {
  const listLength = list.length;
  const arr = [];

  for (let i = listLength - 1; i >= 0; i--) {
    arr.push(list[i]);
  }

  return arr;
};
