from django.shortcuts import render

from .models import Book, Vote



def home(request):
	return render(request, 'index.html')