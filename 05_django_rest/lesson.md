REST API

API : 정해진 형식으로 요청을 보내면 요청한 정보를 받을 수 있는 소통 방법



각 요청이 어떠한 동작 & 정보를 위한 것인지 요청 형식 자체(주소)로 파악이 가능한 것



CRUD	HTTP Method

CREATE : POST

READ : GET

UPDATE : PUT / PATCH

DELETE : 



## fixture

- 데이터베이스의 직렬화(serialiezed) 된 내용을 포함하는 파일 모음이다.
- 각 fixture 는 고유한 이름을 가지며, 이를 구성하는 파일은 여러 응용 프로그램에서 여러 디렉토리에 배포 될 수 있다.
- django 는 `loaddata` 시 설치된 모든 app 에서 `fixtures` 라고 이름의 폴더를 찾는다.

```
musics/
	fixtures/
		musics/
		dummy.json
```

