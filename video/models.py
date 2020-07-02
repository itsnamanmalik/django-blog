from django.db import models
from blog.models import Category

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=80, unique=False)
    video_id = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, unique=False)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    def __str__(self):
        return self.title
