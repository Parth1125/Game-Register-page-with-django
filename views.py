from django.shortcuts import render, resolve_url

# Create your views here.

def index(request):
    return render(request, 'index.html')