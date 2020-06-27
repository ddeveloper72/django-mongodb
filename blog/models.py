from djongo import models
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms


# PROVIDE AN OPTION TO PUBLISH A POST: MANAGED FROM DJANGO ADMIN
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Blog(models.Model):
    # EMBEDDED THE BLOG INTO THE POST DOCUMENT; NO EQUIVALENT SQL TABLE NEEDED
    name = models.CharField(max_length=200, unique=True)
    tagline = models.CharField(max_length=200)

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


class MetaData(models.Model):
    # EMBED METADATA IN POST DOCUMENT; NO EQUIVALENT SQL TABLE IS NEEDED
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

    class Meta:
        ordering = ['updated_on']


class Post(models.Model):
    # POST COLLECTION CONTAINS EMBEDDED METADATA & BLOG DATA,
    # IT REFERENCES EXTERNAL USER MODEL AS WELL AS COMMENT MODEL
    title = models.EmbeddedModelField(
        model_container=Blog,
        model_form_class=BlogForm
    )
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, default=None,
                               related_name="blog_author",
                               on_delete=models.CASCADE)
    meta_data = models.EmbeddedModelField(
        model_container=MetaData,
    )
    headline = models.CharField(max_length=255)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    object_id = models.PositiveIntegerField(default=True)

    # CHALLENGES NOT OVERCOME:
    # BEING ABLE TO REF EMBEDDED FIELDS WOULD BE AN ADVANTAGE FROM HERE
    # IN THIS CASE TO ORDER DATA IN META_DATA > CREATED_ON
    # class Meta:
    #     ordering = ['meta_data__updated_on']

    def __str__(self):
        return self.headline


class Comment(models.Model):
    # COMMENT COLLECTION CONTAINS COMMENT DOCUMENTS RELATING TO EACH POST ID
    name = models.ForeignKey(User, default=None,
                             on_delete=models.CASCADE)
    post = models.ForeignKey(Post, default=None,
                             on_delete=models.CASCADE,
                             )
    comment_text = models.TextField(blank=False)
    approved_comment = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

# ENABLE COMMENT APPROVE FROM DJANGO ADMIN FORM
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.created_on
