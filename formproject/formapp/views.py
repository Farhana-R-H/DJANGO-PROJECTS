
from django.shortcuts import render
from .forms import Myforms

def home(request):
    form = Myforms()
    return render(request, "home.html", {"form": form})

def show_details(request):
    if request.method == "POST":
        form = Myforms(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['name']
            Addr = form.cleaned_data['address']
            Age = form.cleaned_data['age']
            Phn = form.cleaned_data['phoneNo']
            return render(request, 'home.html', {
                'msg': 'Success!',
                'form': form,
                'name': Name,
                'address': Addr,
                'age': Age,
                'phn': Phn
            })
    else:
        form = Myforms()
    
    return render(request, "home.html", {"form": form, "msg": "Please fill the form."})
