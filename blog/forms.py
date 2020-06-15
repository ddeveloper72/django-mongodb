from django import forms
from .models import Post


class BlogForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            'title', 'content', 'content'
        )
        widgets = {
            'title': forms.Textarea(attrs={'placeholder':
                                           'Post Title'}),
            'content': forms.Textarea(attrs={'placeholder':
                                             'About your post here...'})
        }


# class CommentForm(forms.ModelForm):

#     class Meta:
#         model = Comment
#         fields = (
#             'name', 'comment_text'
#         )
#         widgets = {
#             'name': forms.Textarea(attrs={'placeholder':
#                                           'Add your name'}),
#             'comment_text': forms.Textarea(attrs={'placeholder':
#                                                   'Comment on this blog'})
#         }
