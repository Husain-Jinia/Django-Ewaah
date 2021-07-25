from django.shortcuts import render
from .models import Blog 


# Create your views here.
def home(request):
    blog = Blog.objects.all()
    return render(request,'blog/blogpage.html', {"blogs": blog}) 

def viewblog(request,blog_id):
    blogs = Blog.objects.get(id= blog_id)
   
    return render(request, 'blog/ViewBlog.html', 
    {
    "blogs": blogs
    })