from django.contrib import admin

from apps.employees.models import Employee


@admin.register(Employee)
class EmployeAdmin(admin.ModelAdmin):
    pass
