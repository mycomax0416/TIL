const numbers = [1, 2, 3, 4]

numbers[-2] // undefined 정확한 양의 정수 index 만 가능
numbers.length

// 원본 변경
numbers.reverse() // [4, 3, 2, 1]
numbers // [4, 3, 2, 1]

numbers.push(100) // 5 (배열의 길이를 return)
numbers.pop() // 100 (배열의 마지막 요소 제거 후 return)

numbers.shift() // 4 (배열의 첫번째 요소 제거 후 return)
numbers.unshift() // 배열의 첫번째 요소로 값 추가 (길이를 return)

numbers.includes(1) // 값이 있으면 true, 없으면 false

const numbers = [1, 2, 3, 4, 'a', 'a']

numbers.indexOf('a') // 4 => 처음 찾은 요소의 index (중복이 있어도 처음 찾은 요소의 index)
numbers.indexOf(100) // -1 => 찾고자 하는 요소가 없으면 -1


numbers.join() // 1, 2, 3, 4, 'a', 'a'
numbers.join('') // 1234aa
numbers.join('-') // 1-2-3-4-a-a