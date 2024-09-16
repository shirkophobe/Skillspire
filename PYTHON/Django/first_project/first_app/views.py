from django.shortcuts import render, HttpResponse
from datetime import datetime

def index(request):
    return render(request, "index.html")

# def current_datetime(request):
#     # Get the current UTC time
#     utc_now = datetime.utcnow()

#     # Subtract 7 hours to get UTC-7 (equivalent to Pacific Daylight Time, etc.)
#     utc_minus_7 = utc_now - timedelta(hours=7)

#     # Format the date and time
#     formatted_datetime = utc_minus_7.strftime('%b %d, %Y %I:%M %p')

#     # Pass it to the template
#     return render(request, 'time.html', {'datetime': formatted_datetime})

def displayname(request, name):
   return render(request, "name.html" , context = { "name": name } ) 

def displayfood(request, food):
   return render(request, "food.html" , context = { "food": food } ) 

def displayvacation(request, vacation):
   return render(request, "vacation.html" , context = { "vacation": vacation } )
