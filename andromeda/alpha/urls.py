from django.urls import path

from . import views

urlpatterns=[
	path('', views.myview, name='myview'),
	path('likes/', views.likes, name='likes')

]