const word = 'hello\nworld'

console.log(word)

const age = 10
const message = `hello, ${age}
bye`

console.log(message)

// undefined
// 값이 없을 경우 JS 가 자동으로 할당해주는 값

// NULL
// 값이 없음을 우리가 표현하기 위해서 인위적으로 사용하는 값

// 동등 연산자 ==, !=
// 일치 연산자 ===, !==

console.log(3 * null) // 0, null 은 0 으로 인식
console.log('6' - 1) // 5
console.log('6' + 1) // 61
console.log('six' * 3) // NaN

// 논리 연산자
// and &&
// or ||
// not !

// 상황 연산자
// 값 ? true : false
// true ? 1 : 2 // 1
const result = 'ssafy' ? 'class' : 'awesome' // class
