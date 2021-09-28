from django.db import models

# Create your models here.
class Game(models.Model):
	name = models.CharField(max_length=20)
	favorite_game = models.CharField(max_length=20)

	def __str__(self):
		return self.favorite_game