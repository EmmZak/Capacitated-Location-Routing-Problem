# Capacitated-Location-Routing-Problem

The structure of the files is as follows:


number of customers
number of available depots

coordinates for the depots (x and y)

coordinates for the customers

vehicle capacity

depot capacities (for Tuzun instances, each one is equal to the total demand as there is no capacity on the depots)

customers demands

opening costs for the depots

opening cost of a route (cost of a vehicle)

0 or 1 (0 means that the costs are integer - 1 that costs are real)


To calculate the matrix distance (or the cost to link any 2 points A and B in the graph), we use the mathematical formula:

sqrt( (xA-xB)² + (yA-yB)² )

The results are stored in a float variable (in C language) if the costs are real (code 1)
The result is multiplied by 100 and truncked to be stored in an integer variable if the costs are interger (code 0).