from django.core.management.base import BaseCommand
from DataEntryApplication.models import Student
from datetime import date

class Command(BaseCommand):
    help = 'Inserts sample data into the Student model'

    def handle(self, *args, **kwargs):
        # Sample data to insert
        sample_students = [
            {'roll_number': 'S004', 'name': 'Alice Johnson', 'date_of_birth': date(2000, 5, 15)},
            {'roll_number': 'S005', 'name': 'Bob Smith', 'date_of_birth': date(1999, 8, 22)},
            {'roll_number': 'S006', 'name': 'Charlie Brown', 'date_of_birth': date(2001, 12, 3)},
        ]

        for student_data in sample_students:
            student, created = Student.objects.get_or_create(**student_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully inserted: {student}'))
            else:
                self.stdout.write(self.style.WARNING(f'Student already exists: {student}'))