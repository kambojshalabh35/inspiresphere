from django.shortcuts import render

from main.models import StartUps, Resources

# Create your views here.

def home(request):
    startups = StartUps.objects.all()[0:3]
    return render(request, 'main/home.html', {'startups': startups})

def startUps(request):
    startups = StartUps.objects.all()
    return render(request , 'main/startups.html' , {'startups': startups})

def resources(request):
    courses = Resources.objects.all()
    return render(request , 'main/resources.html' , {'courses': courses })