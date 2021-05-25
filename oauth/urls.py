from django.urls import include, path
from . import views
from django.contrib.auth import logout
from django.conf import settings

urlpatterns = [
    path('', views.index, name='oauth'),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', views.logout, name='logout')
]