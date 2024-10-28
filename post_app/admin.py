from django.contrib import admin
from .models import Post

# 관리자 페이지에 출력될 테이블 항목을 아래 필드 형태로 지정
class PostAdmin(admin.ModelAdmin):
  list_display = ['title', 'category', 'created', 'updated']
  
# 관리자 페이지에 PostAdmin 설정이 적용된 Post클래스 모델을 최종 등록
admin.site.register(Post, PostAdmin)