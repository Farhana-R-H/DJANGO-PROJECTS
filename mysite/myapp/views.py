from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,"home.html") 
def index(request):
    return HttpResponse("welcome")
# Create your views here.
