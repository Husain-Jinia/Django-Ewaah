from django.urls import path
from . import views

urlpatterns = [
    path('blogs',views.home, name='blog-home'),
    path('blogs/<int:blog_id>', views.viewblog, name = 'ViewBlog')
]