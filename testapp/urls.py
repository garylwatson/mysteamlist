from django.urls import path
from . import views

#views.py and urls.py in an app map what the user sees to where the user goes
urlpatterns = [
    path("", views.index), #when the user goes to this empty route send them to the index function in views.py
    path("user/", views.user),
    path("profile/", views.profile)
]