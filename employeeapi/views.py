from serializers import EmployeeSerializer
from django.shortcuts import render
from rest_framework.response import Response


# Create your views here.
from .models import Employee


# def put(self, request, *args, **kwargs):
#     emp_object = Employee.objects.get()


#     data = request.data

#     emp_object.fullname = data["fullname"]
#     emp_object.emp_code = data["emp_code"]
#     emp_object.mobile = data["mobile"]
    
#     emp_object.save()

#     serializer = EmployeeSerializer(emp_object)
#     return Response(serializer.data)