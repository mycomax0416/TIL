const test = {
  name: 'ssafy',
  'class number': '123456789', // key 가 여러단어 일 때는 문자열로 작성
  products: {
    ipad: '2019',
    iphone: '11 pro',
    macbook: '2019 pro',
  }
}

test.name
test['name']
// test.class number // 불가능
test['class number']
// test.class_number // 불가능

let brands = ['Apple', 'Samsung',]

let products ={
  'phone': ['iphone', 'galaxy'],
  'laptop': ['macbook', 'series9'],
}

const shop = {
  brands,
  products,
}

console.log(shop)

// JSON

// Object => String
const jsonData = JSON.stringify({ // JSON -> String
  coffee: 'Latte',
  iceCream: 'Mint',
})

console.log(jsonData)
console.log(typeof jsonData) // string

// String -> Object
const parseData = JSON.parse(jsonData)

console.log(parseData)
console.log(typeof parseData) // object