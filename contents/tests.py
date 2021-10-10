from django.test import TestCase
from .models import Content, DRAFT

# Create your tests here.
class ContentTestCase(TestCase):
    
    def setUp(self):
        Content.objects.create(title="joke", author="tester", summary="test joke content")
    
    def test_default_content_status(self):
        joke_content = Content.objects.get(title="joke")
        self.assertEqual(joke_content.status, DRAFT)

    def test_get_author(self):
        joke_content = Content.objects.get(title="joke")
        self.assertEqual(joke_content.author, "tester")