from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
# Create your views here.


def post_list(request):
    context = {}
    posts = Post.objects.all().order_by('-published_date')
    if posts is not None:
        context['posts'] = posts
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    context = {}
    post = get_object_or_404(Post, pk=pk)
    context['post'] = post
    return render(request, 'blog/post_detail.html', context)