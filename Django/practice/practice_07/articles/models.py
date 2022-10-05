from email.policy import default
from random import choices
from django.db import models

# Create your models here.
class Article(models.Model):
    CATEGORY_CHOICES = (
        ("jangsa", "장사소식"),
        ("singsing", "싱싱상회"),
        ("knowhow", "배민노하우"),
    )

    category = models.CharField(
        max_length=10, choices=CATEGORY_CHOICES, default="jangsa"
    )

    title = models.CharField(max_length=80)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
