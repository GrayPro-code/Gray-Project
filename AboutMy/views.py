from django.shortcuts import render
from .models import Posts



def AboutMy(request):
	post = Posts.objects
	return render(request, 'posts/AboutMy.html', {'post': post}) 
