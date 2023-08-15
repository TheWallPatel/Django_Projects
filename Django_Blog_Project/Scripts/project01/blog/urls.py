from django.urls import path
from . import views

urlpatterns = [
    # arg1: route eg-> /admin,/home or empty
    # arg2: url to connect when on route given
    path('', views.home,name="blog-home"),
    path('about/', views.about,name="blog-about"),
]