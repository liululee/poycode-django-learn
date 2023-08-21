from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date  = models.DateTimeField(auto_now_add=True)
    
    def pub_date_valid(self):
        return self.pub_date < timezone.now()


class UserPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.BigIntegerField(name='用户ID')
    read_times = models.BigIntegerField(name='个人点击次数', default=1)
    is_like = models.BooleanField(name = '喜欢', default=False)
    is_start = models.BooleanField(name= '收藏', default=False)
    is_public = models.BooleanField(name='公开', default=True)
