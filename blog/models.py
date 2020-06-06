from djongo import models
from django import forms
from django.utils import timezone
# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=40)
    tagline = models.TextField()
    pub_date = models.DateTimeField(blank=True, null=True,
                                    default=timezone.now)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = (
            'name', 'tagline'
        )
        widgets = {
            'name': forms.Textarea(attrs={'placeholder':
                                          'Blog Title'}),
            'tagline': forms.Textarea(attrs={'placeholder':
                                             'About this Blog'})
        }


class Comment(models.Model):
    name = models.CharField(max_length=40)
    comment_text = models.TextField(max_length=360)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = (
            'name', 'comment_text'
        )
        widgets = {
            'name': forms.Textarea(attrs={'placeholder':
                                          'Add your name'}),
            'comment_text': forms.Textarea(attrs={'placeholder':
                                                  'Comment on this blog'})
        }

# metadata model representing dates and intergers such as pingbacks
# and ratings

class MetaData(models.Model):
    pub_date = models.DateField()
    mod_date = models.DateField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()


# Djongo will never register this model as an actual model. 
    class Meta:
        abstract = True


class MetaDataForm(forms.ModelForm):

    class Meta:
        model = MetaData
        fields = (
            'pub_date', 'mod_date',
            'n_pingbacks', 'rating'
        )
        

class Author(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.EmbeddedModelField(
        model_container=Blog,
        model_form_class=BlogForm
    )
    meta_data = models.EmbeddedModelField(
        model_container=MetaData,
        model_form_class=MetaDataForm
    )
    headline = models.CharField(max_length=80)
    body_text = models.TextField(max_length=360)
    comment = models.EmbeddedModelField(
        model_container=Comment,
        model_form_class=CommentForm
    )
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
 
    def __str__(self):
        return self.headline
