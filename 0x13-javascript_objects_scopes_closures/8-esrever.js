#!/usr/bin/node
exports.esrever = function (list) {
  const mylist = [];
  for (let i = list.length - 1; i > 0; i--) {
    mylist.push(list[i]);
  }
  return mylist;
};
