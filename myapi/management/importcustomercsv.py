from django.core.management.base import BaseCommand, CommandError
from myapi.models import Consumer as Person

class Command(BaseCommand):
    help = 'Imports data from CSV file'
