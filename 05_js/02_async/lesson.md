## 동기식 처리 모델 (Synchronous)

- 직렬적으로 테스크를 수행
- 테스크는 순차적으로 실행되며 어떤 작업이 수행중이면 다음 작업은 대기
- 예) 서버에서 데이터를 가져와서 화면에 표시하는 작업을 수행할 때, 데이터가 응답될 때 까지 이후 테스크들은 블로킹(blocking)된다.

---

## 비동기 처리 모델 (Asynchronous)

- 병렬적으로 테스크를 수행
- 테스크가 종료되지 않은 상태라 하더라도 대기하지 않고 다음 테스크를 실행
- 예) 서버에서 데이터를 가져와서 화면에 표시하는 작업을 수행할 때, 데이터가 응답될 때 까지 기다리지 않고  (non-blocking) 즉시 다음 테스크를 수행
- JS 대부분의 DOM 이벤트와 Timer 함수, Ajax 요청은 비동기식 처리 모델로 동작

---

## Blocking vs non-blocking

### 이벤트 루프

- 단 한가지 **콜스택**과 **콜백큐**를 감시하는 역할만 합니다.
- 만약 콜스택이 비어 있으면 이벤트 루프는 콜백큐에서 첫 번째 이벤트를 가져다가 콜스택에 밀어 넣고, 결과적으로 해당 이벤트가 실행된다.
- 이러한 반복은 이벤트 루프에서 `tick` 이라고 한다.
- 이벤트루프는 호스팅 환경(브라우저 or nodejs)에 내장된 매커니즘 (JS 엔진에 있는게 아니다)
- 이것은 시간의 흐름에 따라 코드의 수행을 처리하며 그때마다 JS 엔진을 작동 시킨다.

---

### setTimeout(mycallback, msecs)

- mycallback 함수가 1초뒤에 실행될 것이다 라는 의미가 아니다.
- **1초 후에 콜백 큐에 초가될 것이라는 의미**
- 만약에 콜백 큐에 mycallback 보다 먼저 추가된 이벤트가 있을수도 있기 때문에 실제 1초보다 더 오랜시간이 걸릴 수도 있다.

---

### Axios

- `axiosXHR `을 요청으로 보내고 응답 받은 결과를 `Promise `객체로 반환 해주는 라이브러리
- axios 는 현재 JS 에서 가장 HOT 한 라이브러리 중 하나이며 프론트 엔드 프레임워크(react, vue) 에서 데이터를 주고 받을 때 필수적으로 사용되고 있음(프론트엔드 프레임워크 <-> api 서버)