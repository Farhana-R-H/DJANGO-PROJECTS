from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


@login_required
def home(request):
    return render(request,"home.html")

def loginview(request):
    uname = request.POST['username']
    pwd = request.POST['password']
    user = authenticate(request, username=uname, password=pwd)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return render(request,"login.html",{"msg":"Invalid login"})
    
def logout_view(request):
    logout(request)
    return redirect('login')    

def add(request):
    Fnum=int(request.GET["txt1"])
    Snum=int(request.GET["txt2"])
    s=Fnum+Snum
    return render(request,"home.html",{"sum":s})



