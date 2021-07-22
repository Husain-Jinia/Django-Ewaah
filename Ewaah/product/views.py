from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'product/home.html', context)


def viewmore(request,product_id):
    products = Post.objects.get(id=product_id)
   
    return render(request, 'product/ViewMore.html', 
    {
    "posts":products
    })