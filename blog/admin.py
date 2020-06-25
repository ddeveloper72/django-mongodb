from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('headline', 'status', 'author')
    list_filter = ("status",)
    search_fields = ['headline', 'content', 'author']
    prepopulated_fields = {'slug': ('headline',)}


admin.site.register(Post, PostAdmin)
