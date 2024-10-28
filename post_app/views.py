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

#해당 view 함수가 GET, POST 요청을 처리할 수 있음을 나타냄
@api_view(['GET', 'POST'])
def posts(request):
  # GET 방식 요청이 들어왔을 때 응답 처리
  if request.method == 'GET':
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
  
  # POST 방식 요청이 들어왔을 때 응답 처리
  elif request.method == 'POST':
    # POST 요청시 같이 들어온 데이터를 역직렬화 처리
    serializer = PostSerializer(data = request.data)
    # 역직렬화화된 데이터 검증
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # 역직렬화된 데이터의 검증 실패시 400 상태값 변환
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)