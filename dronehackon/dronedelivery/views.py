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
    loc["coordinates"] = coords.copy()
    loc["demand"] = 0
    input_data['depot']=loc.copy()
    all_points = np.array([[coords["lat"],coords["long"]]])
    print(input_data)
    for order in Order.objects.all():
        coords["lat"]=order.customer.lat
        coords["long"] = order.customer.long
        loc["coordinates"] = coords.copy()
        loc["demand"]=order.cost
        input_data['customer_{}'.format(order.order_id)]=loc.copy()
        all_points = np.append(all_points,[[coords["lat"], coords["long"]]],axis=0)
    print(input_data)

    # Calculating distance matrix
    dist_matrix = squareform(pdist(all_points, metric=haversine))
    print(dist_matrix)

    return HttpResponse(str(input_data))
