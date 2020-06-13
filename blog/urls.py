from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    re_path(r'^(?P<pk>[a-z\d]+)$', views.BlogDetail,
            name='BlogDetail')
]
