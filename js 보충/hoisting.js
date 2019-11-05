console.log(x) // undefined
var x = 10
console.log(x) // 10

// var x // 1. 선언 + 초기화(undefined)
// console.log(x) // 참조 시 에러가 안남 -> undefined
// x = 10 // 3. 여기서 할당
// console.log(x) // 10

console.log(y)
let y = 10
console.log(y)

// var 할당과정
// 1. 선언 + 초기화(동시 진행)
// 2. 할당

// let 할당과정
// 1. 선언
// TDZ (임시적 사각지대)
// 2. 초기화
// 3. 할당

let y // 1. 선언
console.log(y) // 참조 error -> 초기화 전에 참조하려 해서.
y = 10
console.log(y)