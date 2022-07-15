import django_filters
from rest_framework import viewsets
from rest_framework import filters

from apps.employees.serializers.employees import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = serializer_class.Meta.model.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['isArchive', 'role']
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['name']
