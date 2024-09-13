from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html", context = {})


def displayinfo(request):
    name = "James"
    food = "Thai Cusine"
    movie = "Lawrence of Arabia"
    music = "Jazz"
    
    return HttpResponse(f'Name: {name} Favorite Food: {food} Movie: {movie} Music Genre: {music}')