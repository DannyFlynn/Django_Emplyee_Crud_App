from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Employee
import datetime

# Create your views here.

messages = {}

def employees(request):
    employees_data = Employee.objects.all()
    
    return render(request, 'index.html', {'employees': employees_data, 'messages':  messages})

def create_employee(request):
    global messages
    if request.method == 'POST':
        name = request.POST.get('name')
        department = request.POST.get('department')
        salary = request.POST.get('salary')
        sick_days = 0
        start_date = datetime.date.today()
        position = request.POST.get('position')
        
        new_employee = Employee(name=name, department=department, salary=salary, sick_days=sick_days, start_date=start_date, position=position,  )
        new_employee.save()
        
        messages['success'] = "Create"
        return redirect('success_action')

    
    else:
       
       return render(request, 'create_employee.html')
    

def employee_details(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    
    return render(request, 'employee_details.html', {'employee': employee})
        
def update_employee(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)

    if request.method == 'POST':
        print(request.POST)

        employee.name = request.POST.get('name') if request.POST.get('name')  else employee.name
        employee.department = request.POST.get('department') if request.POST.get('department') else employee.department
        employee.position = request.POST.get('position') if request.POST.get('position') else employee.position
        employee.salary = int(request.POST.get('salary')) if request.POST.get('salary') else employee.salary
        employee.sick_days = int(request.POST.get('sick_days')) if request.POST.get('sick_days') else employee.sick_days

        employee.save()

        return redirect('success_action')

 
    


def delete_employee(request, employee_id):

    if request.method == 'POST':

        employee = get_object_or_404(Employee, id=employee_id)
        employee.delete()

        return redirect('success_action')
    
    else:
        
        return HttpResponse('DELETE')




def success_action(request):
    return HttpResponse('Success! You will be redirected in 3 seconds. <script>setTimeout(function(){ window.location.href = "/"; }, 3000);</script>')



