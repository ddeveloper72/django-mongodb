from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Entry, Blog

# Create your views here.


def blogs(request):
    # create a view that gets all the blog entries and
    # renders them to the markup
    entries = Entry.objects.all()

    return render(request, 'blogs.html', {'entries': entries})
