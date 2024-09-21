from django.shortcuts import render, redirect, get_object_or_404
from .models import Course 

def index(request):
    courses = Course.objects.all().order_by('-date_added')
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name and description:
            Course.objects.create(name=name, description=description)
        return redirect('index')
    return render(request, 'index.html', context={'courses': courses})


def confirm_delete(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('index')
    return render(request, 'confirm_delete.html', {'course': course})
