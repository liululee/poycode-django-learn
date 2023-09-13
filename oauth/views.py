from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm
from django.contrib.admin import models
# Create your views here.

# Django自带框架 用户密码登录
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # 验证用户名密码是否正确
            user = authenticate(username=username, password = password)
            if user:
                login(request, user)
                # 登录成功，跳转到首页
                return redirect('/auth/index')
            else:
                form.add_error(field='username',error='用户名或密码错误！')
        else:
            form.add_error(field='captcha', error='验证码错误')
        return render(request, 'login.html', {'form': form})
    login_form = LoginForm()
    return render(request, 'login.html', {'form': login_form})

# 用户登出
def logout_view(request):
    logout(request)
    return redirect('/auth/login')


# 用户注册
def regisiter_view(request):
    register_form = RegisterForm(request.POST)
    if register_form.is_valid():  # 获取数据
        username = register_form.cleaned_data['username']
        password = register_form.cleaned_data['password']
        confirm_password = register_form.cleaned_data['confirm_password']
        email = register_form.cleaned_data['email']
        if password != confirm_password:  # 判断两次密码是否相同
            message = "两次输入的密码不同！"
            return render(request, 'register.html', locals())
        else:
            same_name_user = models.User.objects.filter(username=username)
            if same_name_user:  # 用户名唯一
                message = '用户名已经存在！'
                return render(request, 'register.html', locals())
            same_email_user = models.User.objects.filter(email=email)
            if same_email_user:  # 邮箱地址唯一
                message = '该邮箱地址已被注册！'
                return render(request, 'register.html', locals())
        # 当一切都OK的情况下，创建新用户
        new_user = models.User.objects.create()
        new_user.username = username
        new_user.password = password  # 使用加密密码
        new_user.email = email
        new_user.save()
        return redirect('/user/login/')  # 自动跳转到登录页面
    else:
        register_form = RegisterForm()
        return render(request, 'register.html', locals())


# 未登录，重定向至登录页
@login_required(login_url='/auth/login')
def index_view(request):
    return render(request, 'index.html')

# 微信扫码登录


# QQ扫码登录


# 支付宝登录
