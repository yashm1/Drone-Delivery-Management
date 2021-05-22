# import geopandas
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
# from geopandas import GeoSeries
# from shapely.geometry import Point, MultiLineString, MultiPoint, Polygon
# from sklearn.cluster import KMeans
import math

# drone dimension and number of drones
max_weight = 2000
number_of_drones = 10
height = 10
width = 10
breadth = 10

inp = [{"weight": 120, "lat": 10, "lon": 10, "height": 1, "width": 1, "breadth": 1}, {
    "weight": 1200, "lat": 10, "lon": 11, "height": 1, "width": 1, "breadth": 1},
    {"weight": 1800, "lat": 10, "lon": 12, "height": 1, "width": 1, "breadth": 1}]


inp_weight = 0
for i in range(len(inp)):
    inp_weight += inp[i]["weight"]

no_of_cluster = math.ceil(inp_weight / max_weight)

print(no_of_cluster)
