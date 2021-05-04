from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='secret'
        )

        self.post = Post.objects.create( # pylint: disable=no-member
            title='A good title',
            body='An interesting body',
            author=self.user
        )

    def test_string_representation(self):
        post = Post(title='A good title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'test user')
        self.assertEqual(f'{self.post.body}', 'An interesting body')

    def test_post_list_views(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'interesting body')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_views(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/1000000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 400)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')