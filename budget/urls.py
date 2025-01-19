from django.urls import path
from . import views
from .views import index


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', index, name='index'),
    path('chatbot/', views.chatbot, name='chatbot'),
]