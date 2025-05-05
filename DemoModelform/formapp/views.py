from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from.forms import CustomerForm
from.models import Customer

def home(request):
    new_form=CustomerForm()
    return render(request,"modelform.html",{"form":new_form})


def addcustomer(request):
    try:
        if request.method=="POST":
            new_form=CustomerForm(request.POST)
            if new_form.is_valid():
                new_form.save()
        return render(request,"modelform.html",{"form":new_form,"msg":"customer added"})
    except Exception as e:
        print(e)
        return HttpResponse("Error")

def updateform(request,cid):
    cust=get_object_or_404(Customer,id=cid)
    if request.method=="POST":
        new_form=CustomerForm(request.POST,instance=cust)
        if new_form.is_valid():
            new_form.save()
            return redirect("home")
    else:
        new_form=CustomerForm(instance=cust)
        return render(request,"modelform.html",{"form":new_form,"cust":cust})
    

        
    

  