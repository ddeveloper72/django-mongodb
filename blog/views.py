from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from django.views import View
from .models import Entry, Blog, BlogForm
from django.utils import timezone
from django.contrib import messages

# Create your views here.


def blogs(request):
    # create a view that gets all the blog entries and
    # renders them to the markup
    try:
        entries = Entry.objects.all()
        return render(request, 'blogs.html', {'entries': entries})

    except:
        return HttpResponse('No blog entries have been added yet')


def BlogDetail(request, pk):
    try:
        entry = get_object_or_404(Entry, pk=pk) if pk else None

        return render(request, "blog_detail.html", {'entry': entry})

    except:
        return HttpResponse('No blog entries have been added')



