"""
URL configuration for poycode project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bbs import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', views.hello, name='hello'),
    path('post/<str:title>', views.get_post, name='post'),
    path('bbs/posts', views.get_posts, name='post_list'),
    path('bbs/post/<str:title>', views.get_post_with_template, name='post_detail'),
    path('bbs/post/404/<str:title>', views.get_post_if_404, name ='post_404_detail'),
    path("bbs/about/", TemplateView.as_view(template_name="about.html")),
]
