from rest_framework import serializers
from myapi.models import Consumer, Address

class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = ('id', 'first_name', 'last_name', 'email_address', 'password', 'address')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'address_street', 'address_country', 'address_house_number', 'address_city')
