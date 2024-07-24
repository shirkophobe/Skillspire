// Create a program that calculates the sum of all of the numbers from 1 to 5 (1+2+3+4+5). 
// The final sum for this program should be 15. (This does not have to be a function). 
// Hint: Use a for loop that starts from 1 to 5. 
// Where are you going to save the sum? 

let sum = 0
for (var counter= 1; counter <=5; counter +=1){
        sum += counter;
}

console.log(sum);



// Create a function that accepts an array as a parameter and multiplies every value in that array by 2. 
// Return the same array at the end of the function. 
// Given [1,2,3,4,5] return [2,4,6,8,10]. Hint: arr[i] = arr[i*2]​

function multiply(array){
    for(var i = 0; i < array.length; i++){
        arr[i] = arr[i]*2
    }

    return array
}

multiply( [1,2,3,4,5] )


// Create a function that accepts an array as a parameter 
// and returns the sum of all the numbers in the array. 
// Given [1,2,3,4,5] return 15.

function sum(array){
    let sum = 0

    for(var i = 0;i<array.length;i++){
        sum += arr[i]
    }

    console.log(sum)
}

sum( [1,2,3,4,5] )