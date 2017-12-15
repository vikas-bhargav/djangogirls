from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here.


def post_list(request):
    context = {}
    posts = Post.objects.all().order_by('-published_date') # (published_date=timezone.now()) # .order_by('published_date')
    if posts is not None:
        context['posts'] = posts
    return render(request, 'blog/post_list.html', context)