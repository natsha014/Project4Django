from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Load test data from fixture'

    def handle(self, *args, **options):
        # Удаляем существующие записи
        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command('loaddata', 'catalog_fixt.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
