`strict mode`

function MyFunc(){
    let x = "foo"
    if (x == "foo"){
        let y = "moo"
    }
console.log(x)
console.log(y)
}
MyFunc()

function doSomething() {
    console.log(a);
    console.log(foo());
    let a = 1;
    function foo() {
      return 2;
    }
  }
  doSomething();