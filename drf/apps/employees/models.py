from django.db import models


class Employee(models.Model):
    name = models.CharField("Имя", max_length=255, unique=True)
    isArchive = models.BooleanField("В архиве", default=False)

    class RoleChoices(models.TextChoices):
        waiter = 'waiter', 'Официант'
        cook = 'cook', 'Повар'
        driver = 'driver', 'Водитель'

    role = models.CharField("Должность", choices=RoleChoices.choices, max_length=255, default=RoleChoices.waiter)
    phone = models.CharField("Телефон", max_length=255, blank=True, default="")
    birthday = models.DateField("День рождения")

    class Meta:
        ordering = ['name']
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.name + '-' + self.get_role_display()
