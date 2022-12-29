from django.urls import path
from . import views

urlpatterns = [
    path('', views.ScanAPIView.as_view()),
    path('<int:pk>/', views.ScanAPIView.as_view()),

    path('test/<int:pk>/<int:is_active>', views.ApiTestView.as_view()),
]

