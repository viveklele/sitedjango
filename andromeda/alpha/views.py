from django.shortcuts import render, get_object_or_404
from .models import Game
from django.http import HttpResponseRedirect
from .form import MyData

def myview(request):
	user_data = Game.objects.all()
	context = {'user_data': user_data}
	return render(request, "alpha/myview.html", context)

def likes(request):
	if request.method == "POST":
		form = MyData(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = MyData

	return render(request, "alpha/form.html", {"form":form})