from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
import datetime
from bbs.models import Post


def save_post(title, content, pub_date):
    return Post.objects.create(title= title, content = content, pub_date = pub_date)

# Create your tests here.
class PostModelTests(TestCase): 
    def test_post_insert_with_future_pub_date(self):

        pub_date = timezone.now() + datetime.timedelta(days=-20)
        # future_post = Post(title = '测试Post', content='测试内容', pub_date=pub_date)
        # self.assertIs(future_post.pub_date_valid(), True)
        future_post = save_post(title = '测试Post', content='测试内容', pub_date=pub_date)
        # 测试路由是否可被访问
        url = reverse("post_detail", args=(future_post.title,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
