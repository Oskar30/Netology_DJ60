import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            new_phone = Phone(
                id = phone['id'],
                name = phone['name'],
                image = phone['image'],
                price = phone['price'],
                release_date = phone['release_date'],
                lte_exists = phone['lte_exists'],
                slug = str(phone['name']).replace(' ', '_') # Доброго времени суток, т.к. в задании csv с списком имен без кириллицы/спец. символов, то в данном случае просто заменил пробелы
            )
            new_phone.save()
        print('import completed')