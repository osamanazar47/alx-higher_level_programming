#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err); // Print the error object if reading fails
      return;
    }
    console.log(data); // Print the file content if reading is successful
});
