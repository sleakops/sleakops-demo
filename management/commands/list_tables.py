from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = "Lista todas las tablas de la base de datos actual"

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            tables = connection.introspection.table_names(cursor)
        for table in tables:
            self.stdout.write(table)
