from django.contrib import admin
from .models import Post, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('headline', 'status', 'author',)
    list_filter = ("status",)
    # FOREIGN KEY SEARCHES MUST REF RELATED FIELD IN FOREIGN DOCUMENT
    search_fields = ['headline', 'content', 'author__username', ]
    prepopulated_fields = {'slug': ('headline',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'approved_comment', 'created_on',)
    list_filter = ("approved_comment",)
    # FOREIGN KEY SEARCHES MUST REF RELATED FIELD IN FOREIGN DOCUMENT
    search_fields = ['comment_text', 'post__headline', 'name__username', ]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
