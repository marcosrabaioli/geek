from django.core.management.base import BaseCommand
import os.path
from django.conf import settings



class Command(BaseCommand):
    help = 'Create new serializer.'

    def add_arguments(self, parser):
        parser.add_argument('--name',
                            type=str,
                            help='The name of serializer.')

    def handle(self, *args, **options):

        if options['name'] is None:
            print("Not possible create serializer without a name.")
        else:
            file_path = os.path.abspath(settings.BASE_DIR) + '/rest_api/Serializers/' + options['name'] + 'Serializer.py'
            print(file_path)
            if os.path.isfile(file_path):
                print("The serializer " + options['name'] + " already exists.")
            else:
                file = open(file_path, 'w+')
                file.writelines("# Write your serializer here.")
                file.close()

                file_views_path = os.path.abspath(settings.BASE_DIR) + '/rest_api/serializers.py'

                file_views = open(file_views_path, 'r')
                lines = file_views.readlines()
                lines.append("\nfrom .Serializers." + str(options['name']) + "Serializer import *")

                file_views = open(file_views_path, 'w')  # Abre novamente o arquivo (escrita)
                file_views.writelines(lines)  # escreva o conteúdo criado anteriormente nele.

                file_views.close()