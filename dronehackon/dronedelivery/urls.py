from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('maps/',views.maps,name='maps'),
    path('warehouse/',views.warehouse,name='warehouse'),
    path('orders/',views.orders,name='orders'),
]
