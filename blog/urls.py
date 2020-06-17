from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.PostList, name='blogs'),
    re_path(r'^new/$', views.create_or_edit_a_post,
            name='new_post'),
    path('<slug:slug>/', views.PostDetail, name='post_detail'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', views.create_or_edit_a_post,
            name='edit'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', views.remove_post,
            name='delete')
]
