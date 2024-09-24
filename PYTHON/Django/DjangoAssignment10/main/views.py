from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def validate_registration_data(first_name, last_name, email):
    if len(first_name) <= 1 or len(last_name) <= 1:
        raise ValidationError('First and last name must be longer than 1 character.')
    
    try:
        validate_email(email)
    except ValidationError:
        raise ValidationError('Enter a valid email address.')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        # Server-side validations
        try:
            validate_registration_data(first_name, last_name, email)
        except ValidationError as e:
            return render(request, 'register.html', {'error': e.message})

        # Register the user
        user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email, password=password)
        login(request, user)
        return redirect('news_feed')  # Redirect to the news feed after successful registration
    else:
        return render(request, 'register.html')

from .models import Post

def news_feed(request):
    if request.method == 'POST':
        content = request.POST['content']
        Post.objects.create(user=request.user, content=content)
        return redirect('news_feed')
    else:
        posts = Post.objects.all().order_by('-created_at')
        return render(request, 'news_feed.html', {'posts': posts})
