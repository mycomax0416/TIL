var x = 30

function get() {
  return x // 30
}

// var result = get(20)

// console.log(result) // 30

function set(value) {
  var x = value // 10
}

set(10)
var result  = get(20)

console.log(result) // 30