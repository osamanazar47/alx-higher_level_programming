#!/usr/bin/node
function factorialLoop(number) {
  let result = 1;
  for (let i = 2; i <= number; i++) {
      result *= i;
  }
  return result;
}

console.log(factorialLoop(process.argv[2]));
