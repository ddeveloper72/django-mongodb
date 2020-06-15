from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from django.views import View
from .models import Post
from .forms import BlogForm
from django.utils import timezone
from django.contrib import messages

# Create your views here.


def PostList(request):
    # create a view that gets all the blog entries and
    # renders them to the markup
    try:
        posts = Post.objects.filter(status=1).order_by('-created_on')
        return render(request, 'blogs.html', {'posts': posts})

    except:
        return HttpResponse('No blog entries have been added yet')


def PostDetail(request, slug):
    try:
        post = get_object_or_404(Post, slug=slug)

        return render(request, "blog_detail.html", {'post': post})

    except:
        return HttpResponse('No blog entries have been added')


def create_or_edit_a_post(request, slug=None):
    # and a new blog to the collection
    
    post = get_object_or_404(Post, slug=slug) if slug else None
    form = BlogForm(request.POST, instance=post)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post = form.save()
            return redirect(PostDetail, post.slug)
        else:
            form = BlogForm(instance=post)
            return render(request, 'add_blog.html', {'form': form})
    else:
        form = BlogForm(instance=post)
        return render(request, 'add_blog.html', {'form': form})
