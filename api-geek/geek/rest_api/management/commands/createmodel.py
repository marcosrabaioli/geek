from django.core.management.base import BaseCommand
import os.path
from django.conf import settings



class Command(BaseCommand):
    help = 'Create new model.'

    def add_arguments(self, parser):
        parser.add_argument('--name',
                            type=str,
                            help='The name of model.')

    def handle(self, *args, **options):

        if options['name'] is None:
            print("Not possible create model without a name.")
        else:
            file_path = os.path.abspath(settings.BASE_DIR) + '/rest_api/Models/' + options['name'] + 'Model.py'
            print(file_path)
            if os.path.isfile(file_path):
                print("The filter " + options['name'] + " already exists.")
            else:
                file = open(file_path, 'w')
                file.writelines("# Write your model here.")
                file.close()

                file_views_path = os.path.abspath(settings.BASE_DIR) + '/rest_api/models.py'

                file_views = open(file_views_path, 'r')
                lines = file_views.readlines()
                lines.append("\nfrom .Models." + str(options['name']) + "Model import *")

                file_views = open(file_views_path, 'w')
                file_views.writelines(lines)

                file_views.close()