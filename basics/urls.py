from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',views.Welcome),
    path('contact',views.contact)
]