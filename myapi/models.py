from django.db import models

# firstName,addressStreet,lastName,addressCountry,
# emailAddress,addressHouseNumber,password,addressCity

# Create your models here.
class Address(models.Model):
    address_street = models.CharField(max_length=43)
    address_country = models.CharField(max_length=40)
    address_house_number = models.SmallIntegerField()
    address_city = models.CharField(max_length=24)

    class Meta:
        ordering = ('address_city',)
        
    # Return Address for Django Admin
    def __str__(self):
        return "%s %s, %s, %s" % (self.address_street,
                                  self.address_house_number,
                                  self.address_city,
                                  self.address_country)

class Consumer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.CharField(max_length=254)
    password = models.CharField(max_length=256)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        ordering = ('last_name',)

    # Return PersonName for Django Admin
    def __str__(self):
        return "%s, %s" % (self.last_name,
                           self.first_name)
