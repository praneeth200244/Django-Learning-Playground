from django.test import TestCase
from django.core.management import call_command
from io import StringIO


class GreetingCommandTests(TestCase):
    def test_greets_multiword_name(self):
        output = StringIO()

        call_command('greeting', 'Aravind', 'Bolar', stdout=output)

        self.assertEqual(output.getvalue(), 'Hello, Aravind Bolar!\n')
