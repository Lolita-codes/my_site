from django.shortcuts import render, get_object_or_404
from .models import Post


def home_page(request):
    # Gets the first three posts after sorting by date in descending order
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })


def all_posts(request):
    my_posts = Post.objects.all().order_by('-date')
    return render(request, 'blog/all-posts.html', {
        'posts': my_posts
    })


def show_post(request, slug):
    # requested_post = Post.objects.get(slug=slug)
    requested_post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html', {
        'post': requested_post,
        'post_tags': requested_post.tags.all()
    })
