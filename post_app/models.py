from django.db import models

class Post(models.Model):
  CATEGORY = (('STUDY','Study'),('DIARY','Diary'),('COMMON','Common')) #튜플형 카테고리
  
  title = models.CharField(max_length=100)
  body = models.TextField()
  # url상에서 글 상세페이지 접속시 필요한 글 고유문자값 (id로도 활용가능)
  slug = models.SlugField(unique=True)
  # 글 저장 시 카테고리 범주 지정 항목 (실제 관리자페이지에서 드롭다운 메뉴 형식으로 표현됨, 기본 선택항목은 COMMON으로 지정)
  category = models.CharField(max_length=10, choices=CATEGORY, default='COMMON')
  # created & updated 처음에는 동일하게 생성
  created = models.DateTimeField(auto_now_add=True) #없던 모델을 새로 생성
  updated = models.DateTimeField(auto_now=True) #기존에 있던 모델중 업데이트 내용 날짜값 기록