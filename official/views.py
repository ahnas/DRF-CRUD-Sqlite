from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from employeeapi.models import Employee
from .forms import EmployeeForm


def index(request):
    employeelist = Employee.objects.all()
    form = EmployeeForm(request.POST or None)
    if request.method == 'POST':
        if request.POST.get('id') != '0':
                editEmployee = Employee.objects.get(id =request.POST.get('id'))
                editEmployee.name = request.POST.get('name')
                editEmployee.type = request.POST.get('type')
                editEmployee.age = int(request.POST.get('age'))
                editEmployee.description = request.POST.get('description')
                editEmployee.save()
                response_data = {
                        "status" : "true",
                        "message" : "Employee Field Edited"
                    }
                return HttpResponse(json.dumps(response_data), content_type='application/javascript')

        else:
            if form.is_valid():
                form.save()
                response_data = {
                    "status" : "true",
                    "title" : "Successfully Added",
                    
                }
            else:
                print (form.errors)
                response_data = {
                    "status" : "false",
                    "title" : "Form validation error",
                }
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_index" : True,
            "employeelist":employeelist,
            "form":form,
        }
    return render(request, 'official/index.html',context)


def deletempl(request,id):
    object = Employee.objects.get(id=id)
    object.delete()
    return redirect("official/index")