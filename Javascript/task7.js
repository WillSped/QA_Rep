`strict mode`

function calc(a,b) {
    return (a-b)
}
console.log(calc(40,13))

function welcome(name, age, gender) {
    return (`My name is ${name}, I am ${age} years old and of gender ${gender}`)
}
console.log(welcome("Felix Cited", 20, "Male"))

powerUp = (n1,n2) => Math.pow(n1,n2);
console.log(powerUp(3,4))