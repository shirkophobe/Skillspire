from django.shortcuts import render, redirect
from django.http import HttpResponse

# Part 1
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Part 2
def greet(request, name):
    return render(request, 'index.html', {'name': name}) 

# Part 3
def contact(request):
    return render(request, 'contact.html')

def submit_contact(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        if not firstname or not lastname or not email or not phone or not message:
            error_message = "All fields are required."
            return render(request, 'contact.html', {'error': error_message})

        return render(request, 'confirmation.html', {
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'phone': phone,
            'message': message
        })

    return HttpResponse("Invalid request method.")

# Part 4
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == 'password':
            request.session['is_logged_in'] = True
            return redirect('/admin')

        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error': error_message})

    return render(request, 'login.html')

def admin_panel(request):
    if request.session.get('is_logged_in'):
        return render(request, 'admin_panel.html', {'logged_in': True})
    else:
        return render(request, 'admin_panel.html', {'logged_in': False})
