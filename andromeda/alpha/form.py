from django import forms
from .models import Game

class MyData(forms.ModelForm):
	class Meta:
		model = Game
		fields = ["name", "favorite_game"]
		labels = {"name":"Name", "favorite_game":"Favorite Game"}

