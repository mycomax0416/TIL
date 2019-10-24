from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/detail/', views.create, name='detail'),
    path('<int:article_pk>/update/', views.update, name='update'),
]
