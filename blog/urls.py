from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='homepage'),
    path('posts', views.posts, name='all-posts'),
    path('posts/<slug:slug>', views.show_post, name='post-details')
]