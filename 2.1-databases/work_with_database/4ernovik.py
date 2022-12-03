import csv
from phones.models import Phone

with open('phones.csv', 'r') as file:
    phones = list(csv.DictReader(file, delimiter=';'))

    for phone in phones:
            
            new_phone = Phone(
            name = phone['name'], 
            image = phone['image'],
            price = phone['price'],
            release_date = phone['release_date'],
            lte_exists = phone['lte_exists']
            )
            new_phone.save()

            #print(new_phone)


