from django.shortcuts import render
from .models import Event,Contest
# Create your views here.

def Home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'index2.html')

def contest(request):

    contest = Contest.objects.all()

    return render(request,'contest.html',{'contest':contest})

def event(request):

    event = Event.objects.all()

    return render(request,'event.html',{'event':event})
