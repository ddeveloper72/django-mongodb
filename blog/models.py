from django.db import models

# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=200)
    tags = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

# metadata model representing dates and intergers such as pingbacks
# and ratings
class MetaData(models.Model):
    pub_date = models.DateField()
    mod_date = models.DateField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    class Meta:
        abstract = True



class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.title
