`strict mode`

let darthVader = {
    allegiance: "empire",
    weapon: "lightsabre",
    sith: true
}
console.log(darthVader)

console.log(`Darth Vader's allegiance is to the ${darthVader.allegiance}`)
console.log(`Darth Vader's weapon of choice is a ${darthVader.weapon}`)
console.log(`Darth Vader is a sith? ${darthVader.sith}`)
console.log(`Darth Vader is a jedi? ${darthVader.sith ? "false" : "true"}`)

let myArray = ["hello","everyone"]
console.log(myArray.length)
console.log(myArray.push("How","Are","You"))
console.log(myArray.length)
console.log(myArray.shift)

for (let y in myArray) {
    console.log(y)
}