#!/usr/bin/node
let numOfCalls = 0;

exports.logMe = function (item) {
  console.log(numOfCalls + ': ' + item);
  numOfCalls++;
};
