from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from .models import Post
# Create your views here.

def index(request):
    all_posts = Post.objects.all()
    return render(request, 'index.html', context={'posts': all_posts})

def addpost(request):
    post = request.POST['post']

    Post.objects.create(post = post)

    return redirect('/')