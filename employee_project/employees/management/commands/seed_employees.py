from django.core.management.base import BaseCommand
from employees.models import Department, Employee, Attendance, Performance
from faker import Faker
import random
from datetime import timedelta, date

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        departments = ['HR', 'IT', 'Sales']
        for dep_name in departments:
            Department.objects.get_or_create(name=dep_name)

        for _ in range(5):
            dept = Department.objects.order_by('?').first()
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.email(),
                department=dept,
                position=fake.job(),
                hire_date=fake.date_between(start_date='-3y', end_date='today'),
                salary=round(random.uniform(30000, 100000), 2),
            )

            for i in range(5):
                Attendance.objects.create(
                    employee=emp,
                    date=fake.date_this_year(),
                    status=random.choice(['Present', 'Absent']),
                )

                Performance.objects.create(
                    employee=emp,
                    month=fake.month_name(),
                    rating=round(random.uniform(1, 5), 1),
                    remarks=fake.sentence(),
                )
