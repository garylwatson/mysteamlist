from django.db import models

class Game(models.Model):
    game_name = models.CharField(max_length=100)
    game_appid = models.IntegerField()
    game_score = models.IntegerField() #-1 = metacritic
    game_genre = models.ManyToManyField('Genre')
    game_categories = models.ManyToManyField('Category')

    def __str__(self):
        return f"{self.game_name} - {self.game_appid} - {self.game_score} - {self.game_genre} - {self.game_categories}"

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.TextField(blank=True, null=True)

class Genre(models.Model):
    genre_name = models.CharField(max_length=100)
    genre_description = models.TextField(blank=True, null=True)

    """
    #Return a formatted tuple 
    def __str__(self):
        return f"{self.name}, {self.appid}, {self.categories}, {self.genre}, {self.score}"
    """
