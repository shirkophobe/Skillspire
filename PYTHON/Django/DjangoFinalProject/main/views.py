from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('news_feed')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('news_feed')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# News Feed (main page after login)
@login_required
def news_feed(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Post.objects.create(content=content, author=request.user, created_at=timezone.now())
            return redirect('news_feed')
    
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'news_feed.html', {'posts': posts})

# Edit Post
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return redirect('news_feed')

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            post.content = content
            post.save()
            return redirect('news_feed')

    return render(request, 'edit_post.html', {'post': post})

# Delete Post
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.author:
        post.delete()
    return redirect('news_feed')
