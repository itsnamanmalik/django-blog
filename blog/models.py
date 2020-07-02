from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = models.ImageField(upload_to='blog/categories',default ='common/placeholder.png')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=False)
    author = models.CharField(max_length=30, unique=False)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = models.ImageField(upload_to='blog',default ='common/placeholder.png')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, unique=False)
    featured = models.BooleanField(default=False)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
