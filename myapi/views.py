from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from myapi.models import Consumer, Address
from myapi.serializers import ConsumerSerializer, AddressSerializer

# Create your views here.
def consumer_list(request):
    """
    List all Consumers
    """
    if request.method == 'GET':
        consumers = Consumer.objects.all()
        serializer = ConsumerSerializer(consumers, many=True)
        return JsonResponse(serializer.data, safe=False)

def consumer_detail(request, pk):
    """
    Retrieve a consumer.
    """
    try:
        consumer = Consumer.objects.get(pk=pk)
    except Consumer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ConsumerSerializer(consumer)
        return JsonResponse(serializer.data)
