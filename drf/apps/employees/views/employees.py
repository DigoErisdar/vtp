from rest_framework import viewsets

from apps.employees.serializers.employees import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = serializer_class.Meta.model.objects.all()
