from django.core.management.base import BaseCommand
from ...seeders import seed


class Command(BaseCommand):
    help = 'Seeds the database.'

    def handle(self, *args, **options):
        seed()