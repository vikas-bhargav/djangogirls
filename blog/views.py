from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
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


def post_new(request):
    form = PostForm()
    context = {}
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        context['form'] = form
    return render(request, 'blog/post_new.html', context)


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_new.html', {'form': form})