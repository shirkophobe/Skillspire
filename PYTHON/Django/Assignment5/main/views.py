from django.shortcuts import render, redirect

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0  # Initialize the counter
    elif not request.session.get('no_increment', False):
        request.session['counter'] += 1  # Increment by 1 on every refresh
    
    # Reset the flag so future refreshes can increment the counter again
    request.session['no_increment'] = False
    return render(request, 'index.html', {'counter': request.session['counter']})

def add_two(request):
    request.session['counter'] += 2
    request.session['no_increment'] = True  # Set the flag to prevent index from adding 1
    return redirect('index')

def reset(request):
    request.session['counter'] = 0
    request.session['no_increment'] = True  # Set the flag to prevent index from adding 1
    return redirect('index')
