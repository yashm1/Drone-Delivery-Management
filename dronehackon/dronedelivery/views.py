from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer,Drone,Order
import pandas as pd
import numpy as np
from scipy.spatial.distance import squareform, pdist
from haversine import haversine
# Create your views here.

def index(request):
    n = len(Customer.objects.all())
    k = 8
    q = 6
    depot_lat = 10
    depot_long = 11
    input_data={}
    input_data['Number_of_customers'] = n
    input_data['max_vehicle_number'] = k
    input_data['vehicle_capacity'] = q
    coords={}
    loc = {}
    coords["lat"]=depot_lat
    coords["long"]=depot_long
    loc["coordinates"] = coords
    loc["demand"] = 0
    input_data['depot']=loc
    for order in Order.objects.all():
        coords["lat"]=order.customer.lat
        coords["long"] = order.customer.long
        loc["coordinates"] = coords
        loc["demand"]=order.cost
        input_data['customer {}'.format(order.id)]=loc
    print(input_data)

    return HttpResponse(str(input_data))
