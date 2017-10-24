from myapi.models import Consumer, Address
from myapi.serializers import ConsumerSerializer, AddressSerializer
from rest_framework import generics

# Create your views here.
class ConsumerList(generics.ListCreateAPIView):
    serializer_class = ConsumerSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned consumers to a given country,
        by filtering against a `country` query parameter in the URL.
        """
        queryset = Consumer.objects.all()
        country = self.request.query_params.get('country', None)
        if country is not None:
            queryset = queryset.filter(address__address_country=country)
        return queryset

class ConsumerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer
