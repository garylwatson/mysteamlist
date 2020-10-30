from django.db import models

# Create your models here.
class  Game(models.Model):
    name = models.CharField(max_length=100)
    appid = models.IntegerField(primary_key=True)
    score = models.IntegerField() #-1 = metacritic

    def __str__(self):
        return f"{self.name} - {self.appid} - {self.score}"

class Categories(models.Model):
    name = models.ForeignKey(Game, on_delete=models.CASCADE)
    categories = models.CharField(max_length=100)

class Genre(models.Model):
    name = models.ForeignKey(Game, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)

    #Return a formatted tuple 
    def __str__(self):
        return f"{self.name}, {self.appid}, {self.categories}, {self.genre}, {self.score}"

