`strict mode`

for (let i = 0; i<=100; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
        console.log("FizzBuzz")
    } else if (i % 5 == 0) {
        console.log("Buzz")
    } else if (i % 3 == 0) {
        console.log("Fizz")
    }
    }

//Shortened version
for (let j =0; j<=100; j++) {
j % 3 == 0 ? console.log("Fizz"): j % 5 == 0 ? console.log("Buzz"): (j % 5 == 0 && j % 3 == 0) ? console.log("FizzBuzz"): ""
}