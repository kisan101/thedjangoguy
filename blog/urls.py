from django.urls import path
from .import views


urlpatterns = [
	path('', views.index, name="index"),
	path('about/', views.about, name="about"),
	path('blog_page/', views.blog_page, name="blog_page")
]