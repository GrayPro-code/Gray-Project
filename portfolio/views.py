from django.shortcuts import render
from .models import Site

# Create your views here.
def addSite(request):
	site = Site.objects
	return render(request, 'portfolio.html', {'site': site})