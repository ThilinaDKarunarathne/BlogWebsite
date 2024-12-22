from django.shortcuts import render,HttpResponse
from . models import Post

# Create your views here.

def bloghome (request):
    allPosts = Post.objects.all()
    contex = {'allPosts': allPosts}
    return render(request,'blog/bloghome.html',contex)

def blogpost (request,slug):
    post = Post.objects.filter(slug=slug).first()
    contex = {'post': post}
    return render(request,'blog/blogpost.html',contex)
