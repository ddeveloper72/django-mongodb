from django.contrib import admin
from .models import Post, Author, Entry

# Register your models here.


admin.site.register([Post, Author, Entry])
