from django.shortcuts import render
from django.http import HttpResponse
from userProfile import loginFcn, buildProfile

from .models import Game, Category, Genre

# Create your views here.
def index(request):
    '''
    context = {
        "games": Game.objects.all()
    }
    '''
    queryDict = request.POST
    resp = dict(queryDict)
    if len(resp) == 3:
        user = resp['user']
        pas = resp['pass']
        rep = loginFcn(user[0], pas[0])
        if rep == "welcome back":
            return render(request, "profile.html")
    elif len(resp) == 7:
        user = resp['user']
        uid = resp['steam']
        pas = resp['pass1']
        rep = buildProfile(user[0], uid[0], pas[0])
    return render(request, "user.html")

'''
def user(request):
    return render(request, "user.html")
'''

def profile(request): #This will eventually become the actual index
    return render(request, "profile.html")

def recommend(request):
    return render(request, "recommend.html")