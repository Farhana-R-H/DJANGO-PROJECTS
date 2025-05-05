from django.shortcuts import render
def home(request):
    return render(request,"vote.html")
def display(request):
    age=int(request.POST["txt1"])
    if age>=18:
        return render(request,"vote.html",{"nme1":"ELIGIBLE"})
    else:
        return render(request,"vote.html",{"nme1":"NOT ELIGIBLE"})


