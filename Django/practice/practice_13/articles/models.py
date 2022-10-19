from django.db import models
from imagekit.models.fields import ProcessedImageField
from imagekit.processors import Thumbnail
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    thumbnail = ProcessedImageField(upload_to='thumbnails/',
                                    blank=True,
                                    processors=[Thumbnail(150, 150)],
                                    format='JPEG',
                                    options={'quality': 100},
                                    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
