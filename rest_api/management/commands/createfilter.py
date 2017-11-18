from django.core.management.base import BaseCommand
import os.path
from django.conf import settings



class Command(BaseCommand):
    help = 'Create new filter.'

    def add_arguments(self, parser):
        parser.add_argument('--name',
                            type=str,
                            help='The name of filter.')

    def handle(self, *args, **options):

        if options['name'] is None:
            print("Not possible create filter without a name.")
        else:
            file_path = os.path.abspath(settings.BASE_DIR) + '/rest_api/Filters/' + options['name'] + 'Filter.py'
            print(file_path)
            if os.path.isfile(file_path):
                print("The filter " + options['name'] + " already exists.")
            else:
                file = open(file_path, 'w+')
                file.writelines("# Write your filter here.")
                file.close()

                file_views_path = os.path.abspath(settings.BASE_DIR) + '/rest_api/filters.py'

                file_views = open(file_views_path, 'r')
                lines = file_views.readlines()
                lines.append("\nfrom .Filters." + str(options['name']) + "Filter import *")

                file_views = open(file_views_path, 'w')  # Abre novamente o arquivo (escrita)
                file_views.writelines(lines)  # escreva o conteúdo criado anteriormente nele.

                file_views.close()