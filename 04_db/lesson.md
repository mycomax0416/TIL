`.` : sqlite3 프로그램의 기능을 실행하는 것

`;` : 세미콜론 까지가 하나의 명령(Query)으로 간주

- SQL 문법은 소문자로 작성해도 된다. (단, 대문자를 권장)
- 하나의 DB 에는 여러개의 table 이 존재한다.

id `INTEGER PRIMARY KEY`: rowid 를 대체

row id 의 최대값은 64비트 8바이트 실수의 최대값

9,22,372,036,854,775,807

INSERT INTO 를 한다면

1. AUTOINCREMENT 가 없을 때 : 중간에 없응 ID 를 재사용하므로 에러가 나지 않을 것.
2. AUTOINCREMENT 가 있을 때 : 최대 레코드를 넘어서기 때문에 에러가 발생.



`.` splite3 프로그램의 기능을 실행하는 것`;` 세미콜론 까지가 하나의 멸령(Query)으로 간주- sql 문법은 소문자로 작성해도 된다.(단, 대문자를 권장)

하나의 DB 에는 여러 개의 table 이 존재한다.id `INTEGER PRIMART KEY `: rowid 를 대체ALTER테이블 이름을 변경 혹은 column 추가ALTER TABLE 현재 이름 RENAME TO 새로운 이름ALTER TABLE table ADD COLUMN column DATATYPE;기존의 데이터가 저장되어 있는 상태에서 새로운 컬럼을 추가하려면기존의 컬럼의 데이터 타입에 NOT NULL 조건때문에 추가가 불가능하다.NOT NULL 조건을 없애던가`DEFAULT value;` 디폴트 값으로 주거나