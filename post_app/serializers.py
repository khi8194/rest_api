# pip install djangorestframework

"""

  CRUD ?
  - DB제어를 위한 4가지 (설계) 개념
  - Create : DB에 데이터 생성 (글쓰기 후 저장)
  - Read : DB 데이터 호출 (글 읽기)
  - Update : DB 데이터 수정 (글 수정 후 저장)
  - Delete : DB 데이터 삭제 (글 삭제)
  
  RESTful API (Representational State Transfer )
  - 제어하려고 하는 자원의 상태값 전송 방식
  - CRUD 구현을 위해서 실제 사용해야 되는 개발 방법론을 지칭
  - HTTP 통신을 위한 메서드 방식 GET, POST, PUT, DELETE
  --- GET : 데이터 조회
  --- POST : 클라이언트로부터 데이터를 전달해서 데이터 생성
  --- PUT : 기존 데이터 변경
  --- DELETE : 데이터 삭제
  
  Django 프레임웍에서 굳이 DRF를 써야되는 이유, DRF가 하는 일
  - 장고 프로젝트 기반의 RESTful API 제작을 돕는 라이브러리 (직렬화, 역직렬화 기능 제공)
  - serializer (직렬화) : 장고의 모델 인스턴스를 클라이언트에 읽기 편하도록 json포맷으로 변환 처리
  - deserializer (역직렬화) : 반대로 클라이언트로부터 전달받은 json 데이터를 장고전용의 모델 인스턴스 구조로 역변환 처리
  - validation (데이터 검증) : 역직렬화시 클라이언트가 보낸 데이터를 필드별로 유효성 검사 처리
  
"""