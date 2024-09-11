from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User

class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.post = Post.objects.create(
            title="Test Post", 
            content="This is a test post", 
            author=self.user
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.content, "This is a test post")
        self.assertEqual(self.post.author.username, "testuser")
