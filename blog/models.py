from djongo import models
# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=200)
    tags = models.TextField()

    # class Meta:
    #     abstract = True

    def __str__(self):
        return self.name

# metadata model representing dates and intergers such as pingbacks
# and ratings

class MetaData(models.Model):
    pub_date = models.DateField()
    mod_date = models.DateField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()


# Djongo will never register this model as an actual model. 
    # class Meta:
    #     abstract = True


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    # Djongo will never register this model as an actual model.
    # class Meta:
    #     abstract = True

    def __str__(self):
        return self.name


class Entry(models.Model):
    # blog = models.EmbeddedField(
    #     model_container=Post,
    # )
    # meta_data = models.EmbeddedField(
    #     model_container=MetaData,
    # )
    title = models.CharField(max_length=255)
    body_text = models.TextField()
    
    # authors = models.ArrayField(
    #     model_container=Author,
    # )
    n_comments = models.IntegerField()
 
    def __str__(self):
        return self.title
