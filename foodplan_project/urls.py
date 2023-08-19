from django.contrib import admin
from django.urls import path, include  # Import 'include' to include your app's URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('foodplan.urls')),  # Include your app's URLs
]
