from django.urls import include, path
from .views import PostViewSet, hello_world, get_post_hello_world
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'posts', PostViewSet)


urlpatterns = [
    path('/hello', hello_world),
    path('/get_post_hello', get_post_hello_world),
    path('/', include(router.urls)),
]