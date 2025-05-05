from django.shortcuts import render
from.models import Product

def home(request):
    return render(request,'image.html')

def Add_product(request):
    name=request.POST["productname"]
    price=request.POST["productprice"]
    description=request.POST["desc"]
    image=request.FILES["Image"]
    prodobj=Product.objects.create(name=name,price=price,description=description,image=image)
    prodobj.save()
    return render(request,"image.html",{"msg" :"products added"})

def display(request):
    products=Product.objects.all()
    return render(request,"view.html",{"products":products})




