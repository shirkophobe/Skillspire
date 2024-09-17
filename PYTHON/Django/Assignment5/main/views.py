from django.shortcuts import render, redirect

def index(request):
    # Check if the 'counter' session variable exists, if not, initialize it to 0
    if 'counter' not in request.session:
        request.session['counter'] = 0
    else:
        # Always increment by 1 when visiting the index page
        request.session['counter'] += 1
    
    # Save the session after modifying it
    request.session.modified = True

    # Pass the counter value to the template
    return render(request, 'index.html', {'counter': request.session['counter']})


def addtwo(request):
    # Check if 'counter' exists in session, if not, initialize it to 0
    if 'counter' not in request.session:
        request.session['counter'] = 0
    else:
        # Increment by 2
        request.session['counter'] += 2
    
    # Reset the flag to ensure normal increment by 1 on refresh
    request.session['addtwo_active'] = False
    request.session.modified = True

    # Redirect back to the index page after updating the counter
    return render(request, 'index.html', {'counter': request.session['counter']})

def reset(request):
    # Reset the counter to 0
    request.session['counter'] = 0
    
    # Ensure normal increment by 1 on refresh
    request.session['addtwo_active'] = False
    request.session.modified = True

    # Redirect back to the index page after resetting the counter
    return render(request, 'index.html', {'counter': request.session['counter']})
