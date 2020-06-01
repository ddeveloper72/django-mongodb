from django.db import models
from taggit.managers import TaggableManager

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    published = models.DateField(auto_now_add=True)
    tags = TaggableManager()
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.title
