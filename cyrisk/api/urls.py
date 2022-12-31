from django.urls import path, include

urlpatterns = [
    path('hosts/', include('hosts.urls')),
    path('scans/', include('scans.urls')),
    path('tags/', include('tags.urls')),
]

