from django.shortcuts import render
from django.http import HttpResponse

from .models import Game, Category, Genre

# Create your views here.
def index(request):
    '''
    context = {
        "games": Game.objects.all()
    }
    '''
    return render(request, "user.html")

'''
def user(request):
    return render(request, "user.html")
'''

def profile(request): #This will eventually become the actual index
    return render(request, "profile.html")