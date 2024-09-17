from django.shortcuts import render

def display_info(request):
    context = {
        'first_name': 'James',
        'last_name': 'Browne',
        'favorite_food': 'Thai Cuisine',
        'favorite_vacation': 'Bora Bora'
    }
    return render(request, 'display_info.html', context)
