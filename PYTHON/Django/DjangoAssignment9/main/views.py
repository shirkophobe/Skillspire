from django.shortcuts import render, redirect, get_object_or_404
from .models import User

# Display all users
def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})

# Show a single user's details
def show(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'show.html', {'user': user})

# Add a new user
def new(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        User.objects.create(first_name=first_name, last_name=last_name, email=email)
        return redirect('/')
    return render(request, 'new.html')

# Edit user
def edit(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect(f'/{user.id}')
    return render(request, 'edit.html', {'user': user})

# Delete user
def destroy(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('/')

