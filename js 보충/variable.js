// let
// 선언은 한번만 가능
// 재할당은 가능
let x = 1
// let x = 2 // already been declared
x = 3
console.log(x)

// const
// const 선언시에 초기값을 생략하면 에러 발생
// const SAMPLE
// 재선언 & 재할당 불가능

const SAMPLE = 7

// SAMPLE = 10

// var SAMPLE = 20
// let SAMPLE = 20

if (SAMPLE === 7) {
  const SAMPLE = 20

  console.log(SAMPLE) // 20
}

// scope
// var(함수 스코프) / let(블럭 스코프)
function varFuc() {
  var x = 10
  if (true) {
    var x = 20
    console.log(x) // 20
  }
  console.log(x) // 20
}

varFuc()