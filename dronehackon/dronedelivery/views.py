from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer,Drone,Order
import pandas as pd
import numpy as np
from scipy.spatial.distance import squareform, pdist
from haversine import haversine

from .vrp import *
# Create your views here.

def index(request):
    n = len(Customer.objects.all())
    k = 3
    q = 1500
    depot_lat = 10
    depot_long = 11
    input_data={}
    input_data['instance_name'] = "Django integration trial"
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
    # print(input_data)
    customers = []
    for order in Order.objects.all():
        coords["lat"]=order.customer.lat
        coords["long"] = order.customer.long
        customers.append([order.customer.lat,order.customer.long])
        loc["coordinates"] = coords.copy()
        loc["demand"]=order.cost
        input_data['customer_{}'.format(order.order_id)]=loc.copy()
        all_points = np.append(all_points,[[coords["lat"], coords["long"]]],axis=0)
    # print(input_data)

    # Calculating distance matrix
    dist_matrix = squareform(pdist(all_points, metric=haversine))
    input_data["distance_matrix"] = dist_matrix
    # print(dist_matrix)

    nsgaObj = nsgaAlgo(input_data)

    # Setting internal variables
    print(nsgaObj.json_instance)

    # Running Algorithm
    nsgaObj.runMain()
    route = nsgaObj.get_solution()
    colorset=["#000000","#0066ff","#cc0000","#009900","#6600cc","#cc00cc","#009999"]
    route_with_color = zip(route,colorset)
    context ={
        "route": route,
        "depot": [depot_lat,depot_long],
        "num_of_drones": len(route),
        "customers": customers,
        "route_with_color": route_with_color,
    }
    return render(request,'vrp.html',context = context)
    # return HttpResponse(str(route_with_color))
