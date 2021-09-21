from django.contrib import admin
from . models import Stock
from . models import Broker
from . models import Customer

# Register your models here.

admin.site.register(Stock)
admin.site.register(Broker)
admin.site.register(Customer)
