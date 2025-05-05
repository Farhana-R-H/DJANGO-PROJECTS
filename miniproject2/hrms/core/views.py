
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Employee, Department
from django.db.models import Count, Avg


@login_required(login_url='login')
def dashboard(request):
    total_employees = Employee.objects.count()
    avg_salary = Employee.objects.aggregate(Avg('salary'))['salary__avg'] or 0
    department_counts = Employee.objects.values('department__name').annotate(count=Count('id'))

    context = {
        'total_employees': total_employees,
        'avg_salary': avg_salary,
        'department_counts': department_counts,
    }
    return render(request, 'dashboard.html', context)



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('employee_list')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'core/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'core/employee_list.html', {'employees': employees})


@login_required(login_url='login')
def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Redirect to Employee List after adding
    else:
        form = EmployeeForm()
    
    return render(request, 'core/add_employee.html', {'form': form}) 


@login_required(login_url='login')
def edit_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'core/edit_employee.html', {'form': form})


@login_required(login_url='login')
def delete_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'core/delete_employee.html', {'employee': employee})


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'core/dashboard.html')


# Create your views here.
