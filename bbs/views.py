from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponse, Http404
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response


from bbs import serializers

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




## rest_framework:  基于函数的视图：@api_view
from rest_framework.decorators import api_view

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

@api_view(['GET', 'POST'])
def get_post_hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got POST data!", "data": request.data})
    return Response({"message": "Hello, world!"})

## rest_framework: ModelViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def get_serializer_class(self):
        # if self.action == 'list':
        return PostSerializer

