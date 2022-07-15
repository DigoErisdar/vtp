import datetime

from apps.employees.models import Employee
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        data = [
            {
                "id": 1,
                "name": "Илья Емельянов",
                "isArchive": False,
                "role": "driver",
                "phone": "+7 (883) 508-3269",
                "birthday": "12.02.1982"
            },
            {
                "id": 2,
                "name": "Александр Ларионов",
                "isArchive": True,
                "role": "waiter",
                "phone": "+7 (823) 440-3602",
                "birthday": "26.01.1986"
            },
            {
                "id": 3,
                "name": "Богдан Давыдов",
                "isArchive": False,
                "role": "driver",
                "phone": "+7 (971) 575-2645",
                "birthday": "29.11.1990"
            },
            {
                "id": 4,
                "name": "Олимпиада Макарова",
                "isArchive": True,
                "role": "waiter",
                "phone": "+7 (945) 447-2286",
                "birthday": "06.01.1987"
            },
            {
                "id": 5,
                "name": "Алла Котова",
                "isArchive": False,
                "role": "cook",
                "phone": "+7 (948) 523-2964",
                "birthday": "26.01.1982"
            },
            {
                "id": 6,
                "name": "Кира Колесникова",
                "isArchive": True,
                "role": "cook",
                "phone": "+7 (929) 592-3637",
                "birthday": "25.02.1972"
            },
            {
                "id": 7,
                "name": "Александр Третьяков",
                "isArchive": False,
                "role": "driver",
                "phone": "+7 (872) 568-2916",
                "birthday": "31.05.1979"
            },
            {
                "id": 8,
                "name": "Пелагея Морозова",
                "isArchive": False,
                "role": "driver",
                "phone": "+7 (977) 521-3479",
                "birthday": "11.09.1981"
            },
            {
                "id": 9,
                "name": "Агафон Громов",
                "isArchive": True,
                "role": "driver",
                "phone": "+7 (868) 569-3159",
                "birthday": "07.06.1988"
            },
            {
                "id": 10,
                "name": "Владлен Тетерин",
                "isArchive": True,
                "role": "driver",
                "phone": "+7 (808) 592-2480",
                "birthday": "20.06.1978"
            },
            {
                "id": 11,
                "name": "Валерий Пестов",
                "isArchive": False,
                "role": "cook",
                "phone": "+7 (899) 403-2387",
                "birthday": "20.01.1987"
            },
            {
                "id": 12,
                "name": "Даниил Кузнецов",
                "isArchive": True,
                "role": "waiter",
                "phone": "+7 (933) 582-2673",
                "birthday": "25.05.1987"
            },
            {
                "id": 13,
                "name": "Фёдор Веселов",
                "isArchive": True,
                "role": "waiter",
                "phone": "+7 (951) 517-3787",
                "birthday": "16.12.1972"
            },
            {
                "id": 14,
                "name": "Пантелеймон Ефимов",
                "isArchive": True,
                "role": "cook",
                "phone": "+7 (807) 492-3627",
                "birthday": "17.04.1986"
            },
            {
                "id": 15,
                "name": "Иванна Калашникова",
                "isArchive": True,
                "role": "waiter",
                "phone": "+7 (927) 488-2568",
                "birthday": "24.03.1982"
            },
            {
                "id": 16,
                "name": "Прасковья Кондратьева",
                "isArchive": True,
                "role": "cook",
                "phone": "+7 (875) 517-3873",
                "birthday": "07.06.1983"
            },
            {
                "id": 17,
                "name": "Евдокия Филиппова",
                "isArchive": False,
                "role": "waiter",
                "phone": "+7 (877) 450-3253",
                "birthday": "03.12.1994"
            }
        ]
        items = []
        for item in data:
            item['birthday'] = datetime.datetime.strptime(item['birthday'], "%d.%m.%Y")
            items.append(Employee(**item))
        Employee.objects.bulk_create(items)
