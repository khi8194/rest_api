from django.urls import path
from .import views

# posts 경로로 url 접속 시 views.py에 등록된 posts REST 응답 함수 매핑
urlpatterns = [
  path('posts', views.posts, name='posts')
]