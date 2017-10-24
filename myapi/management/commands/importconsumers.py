from django.core.management.base import BaseCommand, CommandError
from myapi.models import Consumer
from myapi.models import Address
import csv

class Command(BaseCommand):
    help = 'Imports data according to Consumer/Address model'

    def add_arguments(self, parser):
        parser.add_argument('file_name', nargs='+', type=str)

    def handle(self, *args, **options):
        for filename in options['file_name']:
            # Import CSV file with use of Command argument 'filename'
            with open(filename) as csvfile:
                lines = csv.DictReader(csvfile)
                for line in lines:
                    person = Consumer()
                    #  Match CSV lines to MyApi Model of Consumer and Address
                    person.first_name = line['firstName']
                    person.last_name = line['lastName']
                    person.email_address = line['emailAddress']
                        
                    # Hash password before storing. Can be checked with check_password(password, encoded)
                    person.password = django.contrib.auth.hashers.make_password(line['password'])

                    personaddress = Address()
                    personaddress.address_street = line['addressStreet']
                    personaddress.address_country = line['addressCountry']
                    personaddress.address_house_number = line['addressHouseNumber']
                    personaddress.address_city = line['addressCity']
                    personaddress.save()

                    person.address = personaddress
                    person.save()
