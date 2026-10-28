from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv


# Proposed command: python manage.py importdata "path/to/your/file.csv" model_name
class Command(BaseCommand):
    help = "Imports data from a CSV file into a model"


    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file to import')
        parser.add_argument('model_name', type=str, help='Name of the model to import data into (e.g., Student)')

    def handle(self, *args, **kwargs):
        model_name = kwargs['model_name'].capitalize()  # Ensure the model name is capitalized to match the class name
        model = None 

        for application in apps.get_app_configs():
            try:
                model = apps.get_model(application.label, model_name)
                break
            except LookupError:
                continue

        if model is None:
            raise CommandError(f'Model "{model_name}" not found in any installed application.')
        
        with open(kwargs['file_path'], 'r') as file:
            reader = csv.DictReader(file)
            csv_fields = reader.fieldnames or []

            unique_field = next(
                (
                    field
                    for field in model._meta.fields
                    if field.unique and field.name in csv_fields
                ),
                None,
            )

            if unique_field is None:
                raise CommandError(
                    f'CSV file must include a unique field for model "{model_name}".'
                )
            
            for row in reader:
                lookup = {unique_field.name: row[unique_field.name]}
                defaults = {
                    field_name: value
                    for field_name, value in row.items()
                    if field_name != unique_field.name
                }
                instance, created = model.objects.get_or_create(
                    **lookup,
                    defaults=defaults,
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully imported: {instance}'))
                else:
                    self.stdout.write(self.style.WARNING(f'{model_name} already exists: {instance}'))