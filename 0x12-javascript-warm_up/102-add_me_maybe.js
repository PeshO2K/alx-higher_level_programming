#!/usr/bin/node
exports.addMeMaybe = function incrementAndCall (number, theFunction) {
  number++;
  theFunction(number);
};
