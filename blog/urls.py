from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
    path('all_posts', views.AllPostsView.as_view(), name='all-posts'),
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name='post-details')
]