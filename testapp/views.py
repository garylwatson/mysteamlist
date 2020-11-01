from django.shortcuts import render
from django.http import HttpResponse

from .models import Game, Categories, Genre

# Create your views here.
def index(request):
    context = {
        "games": Game.objects.all()
    }
    return render(request, "testapp/index.html", context)