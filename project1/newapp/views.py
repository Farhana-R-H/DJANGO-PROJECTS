from django.shortcuts import render

def home(request):
    return render(request,"new.html")
def display(request):
    name=request.POST["txt"]
    return render(request,"result.html",{"NME":"WELCOME  "+name}) 

