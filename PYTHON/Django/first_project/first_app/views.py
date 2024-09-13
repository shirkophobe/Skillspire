# views.py
from django.shortcuts import render
from datetime import datetime, timedelta

def current_datetime(request):
    # Get the current UTC time
    utc_now = datetime.utcnow()

    # Subtract 7 hours to get UTC-7 (equivalent to Pacific Daylight Time, etc.)
    utc_minus_7 = utc_now - timedelta(hours=7)

    # Format the date and time
    formatted_datetime = utc_minus_7.strftime('%b %d, %Y %I:%M %p')

    # Pass it to the template
    return render(request, 'time.html', {'datetime': formatted_datetime})
