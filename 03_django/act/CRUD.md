title 20자 제한

content 제한없음

created_at 최초생성일자

updated_at 최종수정일자

객체표현 : title



+DB



--------

# CREATE

1. 글을 쓰는 페이지 view (new)
2. 작성된 글을 받아서 db에 저장하는 역할을 하는 view (create)



글이 보이지 않는 이유는 페이지 자체는 index 가 맞지만 url 은 아직 vreate 에 머물어있다. 왜냐하면 페이지는 전환됐지만 url 은 돌아가지 못했기 때문이다.



### GET -> POST

글을 작성할때 GET 이 아닌 POST 를 쓰는 3가지 이유

1. 사용자는 django에게 **HTML 파일을 줘!(GET)** 가 아니라 **~ 한 레코드(글)을 생성해줘(POST) 이기** 때문에 GET 보다는 POST 요청이 더 알맞다.

2. 데이터는 URL 에 노출되면 안된다. (우리가 URL 에 접근하는 방식은 모두 GET). query 의 형태를 통해 DB schema 를 유추할 수 있게 되고 이는 보안의 측면에서 매우 취약하게 된다.

3. 모델(DB) 를 조작하는 친구는 GET 이 아닌 POST 요청! 왜냐? DB를 수정하는건 매우 중요한 일이고 그에 따른 **최소한의 신원확인**이 필요하다! (GET 으로 동작하게 된다면 악성사용자가 URL 만드로 글을 작성, 수정, 삭제할 수 있게 된다.)

   

--------------

### Redirect

- POST 요청은 HTML 문서를 render 하는게 아니라, `~~좀 처리해줘(요청)` 의 의미이기 때문에 요청을 처리하고 나서의 결과를 보기위한 페이지로 넘겨줘야 한다.



### POST 요청으로 변경 후 변화하는 것

- form 을 통해 전송한 데이터를 받을때도 `request.POST` 로 받아야 한다.
- 글이 작성되면 실제로 URL 에 데이터가 나타나지 않게 된다.
- html 문서를 요청하는게 아니기 때문에 html 문서를 받아볼 수 있는 다른 페이지로 redirect 하게 된다.



DETAIL





# READ



# UPDATE

1. 수정하는 페이지 view (edit)
2. 직접 모델에 수정 요청을 보내는 view (update)



# DELETE