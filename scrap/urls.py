from django.urls import path    #path 모듈을 django.urls부터 import
from . import views

urlpatterns = [
    path('', views.scrap, name='scrap'), 
  # arg1: 도메인형식
  # arg2: render해줄 페이지
  # arg3: name (template 작성시 유용하게 쓰임, 필수아님?)
]