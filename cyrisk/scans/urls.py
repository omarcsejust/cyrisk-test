from django.urls import path
from . import views

urlpatterns = [
    path('', views.ScanAPIView.as_view()),
    path('<int:pk>/', views.ScanAPIView.as_view()),
]

