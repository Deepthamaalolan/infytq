def calculate(distance,no_of_passengers):
    pc=distance/10
    cost=pc*70
    tcost=no_of_passengers*80
    tcost=tcost-cost
    if tcost< 0:
        return -1
    else:
        return tcost
  



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))
