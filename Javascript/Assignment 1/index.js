// Print "Hello World" to the console
console.log("Hello World");

// Print your name and your favorite color to the console
console.log("James Browne Dark Green");

// Print the sum of two numbers to the console (Ex: 2+2 = 4)
console.log(2 + 2);

// Use string concatenation to combine your first and last name. Print this to the console.
var firstName = "James",
  lastName = "Browne";
var wholeName = firstName + lastName;
console.log(wholeName);

// Create a for loop that prints all values from 1-10
{
  for (let i = 1; i <= 10; i++) console.log(i);
}

// Create a for loop that prints the word "Skillspire" 5 times
for (var counter = 1; counter <= 5; counter++) {
  console.log("Skillspire");
}

// Create a for loop that multiplies all values from 1-10 by 2 and print these values out to the console.
for (var i = 1; i <= 10; i++) {
  console.log(i * 2);
}

//  Create a for loop that prints all EVEN values from 1-20
for (var i = 2; i <= 20; i += 2) {
  console.log(i);
}

// Create a for loop that prints all ODD values from 1-20
for (var i = 1; i <= 20; i += 2) {
  console.log(i);
}

// Create a for loop that starts at 1 and ends at 10. If a value is even have the console print out “FIZZ”.
//  If the value is odd have the console print out “BUZZ”.
for (let i = 1; i <= 10; i++) {
  if (i % 2 === 0) {
    console.log("FIZZ");
  } else {
    console.log("BUZZ");
  }
}
