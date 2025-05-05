from django.shortcuts import render,redirect
from.models import Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



@login_required
def home(request):
    return render(request,"form.html")


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


def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        else:
            return render(
                request,
                'signup.html',
                {'form': form, 'msg': 'Invalid signup details', 'errors': form.errors}
            )

    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def reset_password(request):
    return render(request,"reset.html")

def new_password(request):
    uname=request.POST["uname"]
    newpwd=request.POST['password']
    try:
        user=User.objects.get(username=uname)
        if user is not None:
            user.set_password(newpwd)
            user.save()
            return render(request,"reset.html",{"msg2":"new password successfully resetted"})
    except Exception as e:
        print (e)
        return render(request,"reset.html",{"msg2":"resetting failed"})    
    



def addemployee(request):
    empname=request.POST["name"]
    empaddress=request.POST["address"]
    empage=request.POST["age"]
    empobject=Employee(name=empname,address=empaddress,age=empage)
    empobject.save()
    return render(request,"form.html",{"msg":"employee added"})
def display(request):
    empdetails=Employee.objects.all()
    return render(request,"form.html",{'emp':empdetails})
def update_employee(request):
    oldname=request.POST['oldname']
    newname=request.POST['newname']
    Employee.objects.filter(name=oldname).update(name=newname)
    return render(request,"form.html",{"msg1":"employee data updated"})
def delete_employee(request):
    NAME=request.POST["name"]
    Employee.objects.filter(name=NAME).delete()
    return render(request,"form.html",{"msg2":"employee name deleted"})
def singleempview(request,eid):
    emp=Employee.objects.get(id=eid)
    return render(request,"form.html",{"emp1":emp})


