from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory
from io import StringIO

from django.core.management import call_command
from django.test import TestCase
from DataEntryApplication.models import Student


class GreetingCommandTests(TestCase):
    def test_greets_multiword_name(self):
        output = StringIO()

        call_command('greeting', 'Aravind', 'Bolar', stdout=output)

        self.assertEqual(output.getvalue(), 'Hello, Aravind Bolar!\n')


class ImportDataCommandTests(TestCase):
    def test_existing_unique_value_is_not_inserted_again(self):
        existing_student = Student.objects.create(
            roll_number='S004',
            name='Alice Johnson',
            date_of_birth=date(2000, 5, 15),
        )
        csv_content = (
            'roll_number,name,date_of_birth\n'
            'S004,Diana Prince,2000-02-29\n'
            'S005,Ethan Hunt,1998-11-07\n'
        )
        output = StringIO()

        with TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / 'students.csv'
            csv_path.write_text(csv_content, encoding='utf-8')
            call_command('importdata', str(csv_path), 'student', stdout=output)

        self.assertEqual(Student.objects.count(), 2)
        existing_student.refresh_from_db()
        self.assertEqual(existing_student.name, 'Alice Johnson')
        self.assertIn('Student already exists: Alice Johnson', output.getvalue())
        self.assertTrue(Student.objects.filter(roll_number='S005').exists())
