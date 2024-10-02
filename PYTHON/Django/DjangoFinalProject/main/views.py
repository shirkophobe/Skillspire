from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request, 'base.html')

# Register view
def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        # Add a success message
        messages.success(request, "Registration successful! Please log in.")
        return redirect('home')  # Redirect to home after registration
    return render(request, 'register.html', {'form': form, 'title': 'Register', 'button_text': 'Register'})



# Login view
def user_login(request):
    form = AuthenticationForm(request, data=request.POST)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('news_feed')  # Redirect to the news feed page after a successful login

    return render(request, 'login.html', {'form': form, 'title': 'Login', 'button_text': 'Login'})


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
