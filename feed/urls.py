from django.urls import path
from . import views

urlpatterns = [
    # path('', views.fee, name="home"),
    path('feed/', views.feed, name="feed"),
]