from django.contrib import admin
from .models import Author, Entry

# Register your models here.


admin.site.register([Author, Entry])
