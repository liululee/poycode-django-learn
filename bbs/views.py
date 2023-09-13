from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponse, Http404
from bbs.models import Post

# Create your views here.

def hello(request):
    return HttpResponse("hello, Poycode!")

def get_post(request, title):
    post = Post.objects.get(title = title)
    return render(request, 'post.html', {'post': post})

def get_post_with_template(request, title):
    post = Post.objects.get(title = title)
    return render(request, 'post/detail.html', {'post': post})

def get_posts(request):
    posts = Post.objects.all
    return render(request, 'post/index.html', { 'posts': posts })

def get_post_if_404(request, title):
    try:
        post = Post.objects.get(title = title)
    except Post.DoesNotExist:
        raise Http404("Post Not Exist")
    return render(request, 'post/detail.html', {'post': post})

# 便捷写法
def get_post_404(request, title):
    post = get_object_or_404(Post, title=title)
    return render(request , 'post/detail.html', {'post': post})

def index(request):
    print("safdsafdsafdsaf")
    return render(request, 'about.html')