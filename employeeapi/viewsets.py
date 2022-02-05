from rest_framework import routers, serializers, viewsets
from . import models
from . import serializers

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

# list(), retrive(), create(), update(), destroy()