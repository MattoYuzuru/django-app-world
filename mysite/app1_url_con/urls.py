from django.urls import path, re_path
from . import views


app_name = 'app1'
urlpatterns = [
    path('', views.index_page, name='index'),
    path('post/', views.post_page, name='post'),
]
