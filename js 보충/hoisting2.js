if (x !== 1) {
  console.log(y) // undefined
  var y = 3
  if (y === 3) {
    var x = 1
  }
  console.log(y) // 3
}
if (x === 1) {
  console.log(y) // 3
}