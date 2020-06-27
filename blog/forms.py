from django import forms
from .models import Post, Comment


class BlogForm(forms.ModelForm):

    class Meta:
        model = Post
        # author field references auth_user > username for this demonstration
        # so a user can be selected when add in a new blog post.
        fields = (
            'title', 'headline', 'content', 'author', 'status', 'meta_data',
        )
        widgets = {
            'content': forms.Textarea(attrs={'placeholder':
                                             'About your post here...'})
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # author field references auth_user > username for this demonstration
        # so a user can be selected when add in a new post comment.
        fields = (
            'name', 'comment_text',
        )
        widgets = {
            'comment_text': forms.Textarea(attrs={'placeholder':
                                                  'Comment on this blog'})
        }
