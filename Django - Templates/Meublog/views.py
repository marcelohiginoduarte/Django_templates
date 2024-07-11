from django.shortcuts import render
from .models import post

def home(request):
    posts = post.objects.all()
    return render(request, 'Index.html', {'posts':posts})
