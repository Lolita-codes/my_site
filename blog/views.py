from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .form import CommentForm
from .models import Post


class HomeView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query[:3]
        return data


class AllPostsView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'


class PostDetailView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': CommentForm()
        }
        return render(request, 'blog/post-detail.html', context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post-details', args=[slug]))
        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': comment_form
        }
        return render(request, 'blog/post-detail.html', context)
