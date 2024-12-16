from django.shortcuts import render,HttpResponse

# Create your views here.

def bloghome (index):
    return HttpResponse("This is a blog Home page")

def blogpost (request,slug):
    return HttpResponse(f'This is the blog post : {slug}')
