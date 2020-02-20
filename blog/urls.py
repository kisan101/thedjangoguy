from django.urls import path
from .views import about,blog_page,PostListView,PostDetailView


urlpatterns = [
    path('', PostListView.as_view(), name="home"),
    path('about/',about, name="about"),
    path('post/<uuid:pk>/', PostDetailView.as_view(), name="post_detail")
]
