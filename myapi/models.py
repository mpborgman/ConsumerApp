from django.db import models

# firstName,addressStreet,lastName,addressCountry,
# emailAddress,addressHouseNumber,password,addressCity

# Create your models here.
class Consumer(models.Model):
    ID = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.CharField(max_length=254)
    password = models.CharField(max_length=30)

class address(models.Model):
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    address_street = models.CharField(max_length=43)
    address_country = models.CharField(max_length=40)
    address_house_number = models.SmallIntegerField()
    address_city = models.CharField(max_length=24)
