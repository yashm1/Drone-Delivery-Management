# Hackon
Drone Delivery Management

## Problem Statement
In the entire supply chain, the final leg of the delivery- last-mile delivery is the biggest cost driver that accounts for 30% of the supply chain costs. It is also one of the most labour-intensive and time-consuming part of a delivery network.
Therefore, the next big step in delivery services is drone-based delivery. A major pain point for advancement in this area is the efficient routing and distribution of delivery jobs to a fleet of drones

## Solution 
1. Automate the delivery Managment System. Reducing overall delivery cost and optimization of the battery usage. We calculate the most efficient path using the  capacitated vehicle routing problem (CVRP) along with the Genetic algorithm. The capacitated vehicle routing problem (CVRP) is a VRP in which vehicles with limited carrying capacity need to pick up or deliver items at various locations.   
2. We have taken special care to give priority to the Emergency delivery and Prime customer
3. The code shows the real time tracking of the drone in the google maps

## To run this project on your machine:

1. Create a virtual environment somewhere in your project directory and activate it.
```
python3 -m venv venv
source venv/bin/activate
```
2. Install all dependencies from requirements.txt
```
pip install -r requirements.txt
```
3. Now makemigrations and run them.
```
cd dronehackon
python manage.py makemigrations
python manage.py migrate
```
4. Create super user
```
python manage.py createsuperuser
```
5. Run local test server.
```
python manage.py runserver
```

## Contributors
* [Yash Mantri](https://github.com/yashm1)
* [Vishwesh Pillai](https://github.com/theViz343)
* [Shraddha Bhagawat](https://github.com/shraddhab29)
* [Diplesh Mankape](https://github.com/dips4982)
