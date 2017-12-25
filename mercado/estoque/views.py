from django.shortcuts import render

def index(request):
    return render(request, 'estoque/home.html')
