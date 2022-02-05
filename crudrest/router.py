from employeeapi.viewsets import EmployeeViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', EmployeeViewset)

# localhost:port/api/    =   http://127.0.0.1:8000/api/employee/
# GET, POST, UPDATE, DELETE