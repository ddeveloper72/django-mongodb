from djongo import models
from django import forms
# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=40)
    tagline = models.TextField()

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
                                          'Your name please'}),
            'tagline': forms.Textarea(attrs={'placeholder':
                                             'add tags here'})
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
    authors = models.ManyToManyField(Author)
    
    def no_of_comments(self):
        n_comments = Entry.objects.filter(blog=self)
        return len(n_comments)
 
    def __str__(self):
        return self.headline
