from django.urls import path
from . import views

urlpatterns = [
    path('number/', views.number),
    path('result/', views.result),
]
