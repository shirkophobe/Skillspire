from django.shortcuts import render, redirect, get_object_or_404
from .models import User

def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users': users})

def create_user(request):
    if request.method == "POST":
        name = request.POST.get('name')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        diet_preference = request.POST.get('diet_preference')

        user = User(name=name, height=height, weight=weight, diet_preference=diet_preference)
        user.save()

        return redirect('home')
    return render(request, 'create_user.html')

def user_detail(request, id):  # Add this view
    user = get_object_or_404(User, id=id)
    return render(request, 'user_detail.html', {'user': user})
