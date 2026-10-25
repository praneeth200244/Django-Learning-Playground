from django.core.management.base import BaseCommand

# python manage.py greeting "Aravind Bolar" "Kundapura Udupi" - To handle multiple arguments
class Command(BaseCommand):
    help = 'Greets the user'

    def add_arguments(self, parser):
        parser.add_argument('name', nargs='+', type=str, help='Name of the user to greet')

    def handle(self, *args, **kwargs):
        name = ' '.join(kwargs['name'])
        self.stdout.write(self.style.SUCCESS(f'Hello, {name}!'))