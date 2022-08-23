from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='homepage'),
    path('all_posts', views.all_posts, name='all-posts'),
    path('posts/<slug:slug>', views.show_post, name='post-details')
]