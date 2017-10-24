from django.contrib import admin

# Register your models here.
from .models import Consumer
from .models import Address

admin.site.register(Consumer)
admin.site.register(Address)
