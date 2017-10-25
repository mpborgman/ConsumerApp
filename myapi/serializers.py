from rest_framework import serializers
from myapi.models import Consumer, Address

# Make use of Model Serializer
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'address_street', 'address_country', 'address_house_number', 'address_city')

class ConsumerSerializer(serializers.ModelSerializer):
    # Address as nested relation to Consumer
    address = AddressSerializer(many=False, read_only=True)
    
    class Meta:
        model = Consumer
        fields = ('id', 'first_name', 'last_name', 'email_address', 'password', 'address')
