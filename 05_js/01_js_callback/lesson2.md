## JS 함수는 일급객체

## 1. 변수에 담을 수 있다.

## 2. 인자로 전달할 수 있다.

## 3. 반환값으로 전달할 수 있다.

## return n => n + 1



setTimeout



## 비동기식 처리 모델

- 호출될 함수 (콜백함수)를 미리 매개변수에 전달하고 처리가 종료되면 콜백함수를 호출하는 것.

---

## 이벤트 리스너

##### `EventTarget.addEventListener(type, listener)`

1. ##### 무엇을 (버튼을)

2. ##### 언제 (클릭했을 때)

3. ##### 어떻게 (콘솔에 로그를) - listener

---

JS 코드를 body 의 최하단에 위치하는 이유

1. JS 를 읽는 시간 때문에 BODY 안에 있는 HTML 요소들이 브라우저에 그려지는게 지연 될 수 있기 때문.
2. JS 에서 특정 HTML 요소들을 읽고 이벤트를 등록해야 할 때, JS 코드가 먼저 해석되면 해당 요소가 없다고 인식되어 이벤트 등록이 되지 않을 수 있기 때문.

---

querySelector 는 위에서 선택자로 요소를 찾으며 가장 먼저 찾아지는 요소를 반환(단수)

querySelectorAll 은 위에서부터 선택자로 요소를 찾으며 일치하는 요소들을 모두 반환(복수)







키보드 이벤트