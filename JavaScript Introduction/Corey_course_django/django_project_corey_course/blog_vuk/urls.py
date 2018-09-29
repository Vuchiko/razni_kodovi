from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='vuk-blog-home'),
    path('about/', views.about, name='vuk-blog-about'),
]