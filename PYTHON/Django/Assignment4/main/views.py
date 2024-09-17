from django.shortcuts import render

# Parts 1 & 2
def display_info(request):
    context = {
        'first_name': 'James',
        'last_name': 'Browne',
        'favorite_food': 'Thai Cuisine',
        'favorite_vacation': 'Bora Bora',
        'numbers': range(1, 11)  
    }
    return render(request, 'display_info.html', context)

# Part 3 
def submit_form(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        favorite_food = request.POST.get('favorite_food')

        context = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'favorite_food': favorite_food
        }
        return render(request, 'submitted_data.html', context)
    return render(request, 'form.html')

