from django.contrib import admin
from .models import Drone,Customer,Order
# Register your models here.
admin.site.register(Drone)
admin.site.register(Customer)
admin.site.register(Order)