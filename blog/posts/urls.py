from . import views
from django.urls import path

urlpatterns = [
    path('',  views.index, name='index'),
    path('post/<str:pk>', views.Post, name='posts') 
]
