from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('', include('basicConcepts.urls')),
    path('', include('irisApp.urls')),
    path('', include('basics.urls')),
    path('admin/', admin.site.urls),
]
