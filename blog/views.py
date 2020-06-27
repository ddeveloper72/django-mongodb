from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from django.views import View
from django.template.defaultfilters import slugify
from blog.models import Post, MetaData, Comment
from blog.forms import BlogForm, CommentForm
from django.utils import timezone
from django.contrib import messages

# Create your views here.


def PostList(request):
    # create a view that gets all the blog entries and
    # renders them to the markup
    try:      
        posts = Post.objects.filter(status=1)
        comments = Comment.objects.filter(
            approved_comment=True)  # .order_by('-created_on')
        # .orderby('-meta_data__updated_on')
        #  posts are not ordered by updated_on; unable to reach embedded model
        return render(request, 'blogs.html', {'posts': posts,
                                              'comments': comments})

    except:
        #  build return HttpResponse('No blog entries have been added yet')
        return redirect(reverse('PostList'))


def PostDetail(request, slug):
    try:
        post = get_object_or_404(Post, slug=slug)
        comments = Comment.objects.filter(
            approved_comment=True)

        return render(request, "blog_detail.html", {'post': post,
                                                    'comments': comments})
    except:
        #  build return HttpResponse('No blog entries have been added')
        return redirect(reverse('PostList'))


def create_or_edit_a_post(request, slug=None):
    # and a new blog to the collection

    post = get_object_or_404(Post, slug=slug) if slug else None
    form = BlogForm(request.POST, instance=post)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.meta_data.updated_on = timezone.now()
            post = form.save()
            return redirect(PostDetail, post.slug)
        else:
            form = BlogForm(instance=post)
            return render(request, 'add_blog.html', {'form': form})
    else:
        form = BlogForm(instance=post)
        return render(request, 'add_blog.html', {'form': form})


def remove_post(request, slug):
    # remove a post from the collection

    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        post.delete()
        return redirect(reverse('blogs'))
    context = {
        'post': post
    }
    return (render(request, 'remove_blog.html', context))


def add_comment(request, pk):
    # add comment to post
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            post.meta_data.updated_on = timezone.now()
            post.save()
            return redirect(PostDetail, post.slug)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})
