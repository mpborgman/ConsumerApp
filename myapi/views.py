from myapi.models import Consumer, Address
from myapi.serializers import ConsumerSerializer, AddressSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

class MyResultsSetPagination(PageNumberPagination):
    page_size_query_param = 'ps'
    max_page_size = 100

# One generic view to list all consumers, optionally filtered by country
class ConsumerList(generics.ListCreateAPIView):
    # Use Model Serializer
    serializer_class = ConsumerSerializer
    # Make use of DRF pagination through class override
    pagination_class = MyResultsSetPagination

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
    # Use Model Serializer
    serializer_class = ConsumerSerializer
