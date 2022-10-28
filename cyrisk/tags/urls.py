from django.urls import path
from . import views

urlpatterns = [
    path('', views.TagAPIView.as_view()),
    path('<int:pk>/', views.TagAPIView.as_view()),
]

