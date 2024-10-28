from django.shortcuts import render
from post_app.models import Post
# PostSerializer : Post 모델을 직렬화, 역직렬화시 필요한 클래스
from post_app.serializers import PostSerializer
# Response : DRF에서 제공하는 응답 객체로 json형식의 응답을 쉽게 반환처리
from rest_framework.response import Response
# api_view : DRF에서 HTTP메서드 (GET, POST, PUT, DELETE)를 처리하도록 뷰 정의
from rest_framework.decorators import api_view
# status : HTTP통신 상대 코드를 제공하는 모듈, 성공이나 오류에 대한 상대 정보를 제공
from rest_framework import status