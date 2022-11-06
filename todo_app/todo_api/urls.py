from django.urls import re_path, include
from .views import (
    TodoListAPIView,
    TodoDetailAPIView
)

urlpatterns = [
    re_path('api/', TodoListAPIView.as_view()),
    re_path('api/<int:id>/', TodoDetailAPIView.as_view()),
]
