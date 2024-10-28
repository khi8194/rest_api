from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string

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
  
  # Post 클래스에서 생성되는 인스턴스 모델의 타이틀 값을 문자열로 반환
  def __str__(self): # 장고전용 instance객체
    return self.title
  
  # 해당 클래스가 생성하는 모델 인스턴스로 저장해주는 함수
  def save(self, *args, **kwargs):
    # 모델 인스턴스 생성시 slug 항목이 없으면 제목값을 slug화 해서 대신 저장해주는 기능
    if not self.slug:
      slug_base = slugify(self.title)
      slug = slug_base
    
    # 이미 DB상의 같은 항목의 slug 게시글이 존재하면 
    # 기존 slug 이름에 랜덤한 5글자 고유 문자값을 적용하여 slug 중복피함  
    if Post.objects.filter(slug=slug).exists():
      #위의 조건문으로 중복회피한 새로운 슬러그를 인스턴스에 적용
      slug = f'{slug_base}-{get_random_string(5)}'
    self.slug = slugify
    
    #부모 클래스의 save함수를 super를 이용하여 위의 적용 내용들을 반환해서 호출 및 저장
    super(Post,self).save(*args, **kwargs)
