# Dummy model of Uber and Cabs market

to run, just run it on python `python main.py`

## Description

This model will only allow to be asigned a taxi or an Uber, the Persons can request both but will get only one as a response.

## Flow of events
![events flow](others/img/Events.png?raw=true "Event flow")

## The types of events are:
0. Neutral
1. Ask for driver 
2. Search for driver 
3. Asign Driver 
4. Driver arrives at initial point
7. Person takes driver 
6. Arrives at destination 
5. Driver is free 
8. End simulation

##Filters to asign a driver
* Between 5km 
* Closest

##Uber policies
This are the policies which uber can implement in order to run different experiments in **this model**

* Assign policy on driver availability event: asing the free uber to the first user and not the closest  
