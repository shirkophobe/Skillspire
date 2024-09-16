from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")
 
def displayname(request, name):
   return render(request, "name.html" , context = { "name": name } ) 

def displayfood(request, food):
   return render(request, "food.html" , context = { "food": food } ) 

def displayvacation(request, vacation):
   return render(request, "vacation.html" , context = { "vacation": vacation } )  