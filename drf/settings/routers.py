from rest_framework import routers

from apps.employees.views.employees import EmployeeViewSet

router = routers.SimpleRouter()
router.register('employees', EmployeeViewSet, basename="employees")

