from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer,Drone,Order, Depot
import pandas as pd
import numpy as np
from scipy.spatial.distance import squareform, pdist
from haversine import haversine

from .vrp import *
# Create your views here.

def maps(request):
    n = len(Customer.objects.all())
    drone = Drone.objects.get(name = "Test drone")
    depot = Depot.objects.get(name = "Test Depot")
    depot_lat = depot.lat
    depot_long = depot.long
    input_data={}
    input_data['instance_name'] = "Django integration trial"
    input_data['Number_of_customers'] = n
    input_data['max_vehicle_number'] = drone.number
    input_data['vehicle_capacity'] = drone.capacity
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
    drone_params = {
        'weight': drone.weight,
        'capacity': drone.capacity,
        'number': drone.number,
        'bat_consum_perkm_perkg': drone.battery_consumption_perKM_perKg,
        'takeoff_landing': drone.takeoff_landing_consumption,
    }
    nsgaObj = nsgaAlgo(input_data,drone_params)

    # Setting internal variables
    print(nsgaObj.json_instance)

    # Running Algorithm
    route=[]
    if request.method == "POST":
        if "calculation" in request.POST:
            nsgaObj.runMain()
            route = nsgaObj.get_solution()
            request.session['route'] = route
            request.session.modified = True
        elif "animation" in request.POST:
            route = request.session['route']
    colorset=["#000000","#0066ff","#cc0000","#009900","#6600cc","#cc00cc","#009999"]
    route_with_color = zip(route,colorset)
    context ={
        "route": route,
        "depot": [depot_lat,depot_long],
        "num_of_drones": len(route),
        "customers": customers,
        "route_with_color": route_with_color,
    }
    return render(request,'maps.html',context = context)
    # return HttpResponse(str(route_with_color))

def index(request):
    drone = Drone.objects.get(name="Test drone")
    depot = Depot.objects.get(name="Test Depot")
    if request.method == "POST":
        print(request.POST)
        if "update_drone" in request.POST:
            drone.battery = request.POST.get("battery")
            drone.weight = request.POST.get("weight")
            drone.capacity = request.POST.get("capacity")
            drone.battery_consumption_perKM_perKg = request.POST.get("battery_consumption")
            drone.takeoff_landing_consumption = request.POST.get("takeofflanding")
            drone.number = request.POST.get("number")
            drone.save()
        elif "update_warehouse" in request.POST:
            depot.lat = request.POST.get("lat")
            depot.long = request.POST.get("long")
            depot.save()

    depot_lat = depot.lat
    depot_long = depot.long
    return render(request,'index.html',context={
        "drone":drone,
        "depot_lat":depot_lat,
        "depot_long":depot_long,
    })

def warehouse(request):
    return render(request,'profile.html',context={})

def orders(request):
    orders = Order.objects.all()
    return render(request,'table.html',context={"orders": orders})
