from django.urls import path
from . import views

urlpatterns = [
    path('', views.HostAPIView.as_view()),
    path('<int:pk>/', views.HostAPIView.as_view()),
]