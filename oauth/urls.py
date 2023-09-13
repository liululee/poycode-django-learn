from django.urls import re_path as url
from .views import login_view, index_view, logout_view

urlpatterns = [
    url(r'login', login_view),
    url(r'logout', logout_view),
    url(r'index', index_view)
]