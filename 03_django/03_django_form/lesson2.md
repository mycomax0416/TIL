## sign up

- user 를 create

## login

- session 을 create

## logout

- session 을 delete



#### 로그인 사용자에 대한 접근 제한

- django 는 세션과 미들웨어를 통해 인증 시스템을 request 객체에 연결한다.
- request 는 현재 사용자를 나타내는 모든 요청에서 `request.user` 를 제공한다.

`is_authenticated`

- User model 의 속성(attributes)들 중 하나.
- 사용자가 인증 되었는지 알 수 있는 방법
- User 에는 항상 True / AnonymousUser 에 대해서만 항상 False
- 단, 이것은 권한(permission)과는 관련이 없으며 사용자가 활동중(active)이거나 유효한 세션(valid session)을 가지고 있는지도 확인하지 않는다.
- 일반적으로 `request.user` 에서 이 속성을 사용하여 미들웨어의 `django.contrib.auth.middleware.AuthenticationMiddleware` 를 통과했는지 확인한다.



## `next` query string parameter

- @login_required 데코레이터가 기본적으로 인증 성공 후 사용자가 리다이렉트 할 경로를 next 라는 문자열 매개 변수에 저장한다.
- 우리가 url 로 접근하려고 했던 그 주소가 로그인하지 않으면 볼 수 없는 곳이라서, django 가 로그인 페이지로 강제로 리다이렉트 했는데, 로그인을 다시 정상적으로 하고 나면 원래 요청했던 주소로 보내주기 위해 keep 해주는 것.

---

### @required_POST 가 있는 함수에 @login_required 가 설정된다면 로그인 이후 "next" 매개변수를 따라 해당 함수로 다시 redirect 되면서 @required_POST 때문에 405 에러가 발생.



## 회원 탈퇴

article_delete

request

## 회원 수정

## 비밀번호 변경

- 비밀번호 변경 후 로그아웃 되버림.
- 비밀번호가 변경되면서 기존 세션과의 회원 인증 정보가 일치하지 않게 되어 버렸기 때문.

`update_session_auth_hash`

- 현재 사용자의 인증 세션이 무효화 되는 것을 막고, 세션을 유지한 상태로 업데이트.
- 현재 request 와 새로운 session hash 가 생긴 업데이트 된 user 객체를 적절히 업데이트.

## templates정리



get_user_model()

- `User` 를 직접 참조하는 대신 `django.contrib.auth.get_user_model()` 를 사용하여 User model 을 참조해야 한다.
- 이 함수는 현재 활성화(active) 된 User model 을 return 한다.





## Authentication(인증) - 신원 확인

- 자신이 누구라고 주장하는 사람의 신원을 확인하는 것

## Authorization(권한, 허가) - 권한 부여

- 가고 싶은 곳으로 가도록 혹은 원하는 정보를 얻도록 허용하는 과정

