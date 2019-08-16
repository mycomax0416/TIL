csrf 사이트간 요청 위조

웹 어플리케이션 취약점 중 하나로 사용자가 자신의 의도와 무관하게 공격자가 의도한 행동을 해서 특정 웹페이지의 보안을 무력화 시키거나, 수정, 삭제 등의 강제적인 작업을 하게하는 공격 방법.



django 는 최소한의 안전장치를 위해 자신이 부여한 랜덤 hash 값을 token 으로 부여한다. 이 token 값이 없는 요청은 잘못된 요청이라고 판단하여 접근을 거부한다.(403 error)



## static 정적 파일

image / css / js 파일과 같이 해당 내용이 고정되어 응답을 할 때 별도의 처리 없이 그대로 보여주면 되는 파일들





## Django namespace

templates / static



pages/index.html



## Template Ingeritance (상속)



Dont

Repeat

Yourself



1. form(GET/POST)

2. POST - csrf_token

3. static (load, {% static %})

4. URL 로직 (프로젝트 & 앱)

5. Namespace(template, static)
6. 상속(block)