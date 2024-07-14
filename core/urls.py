
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('school_management.urls')),
    path('teacher', include('teacher.urls')),
]
