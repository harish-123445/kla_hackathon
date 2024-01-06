import json
f = open('kla_hackathon/Student_Handout/Input_data/level2a.json')
d = json.load(f)
neighbour=d['neighbourhoods']
ord_quantity=[]
distance=[]
for i in neighbour.keys():
    temp=list(neighbour[i].values())
    ord_quantity.append(temp[0])
    distance.append(temp[1])

res_dist=d['restaurants']['r0']['neighbourhood_distance']

scooter_cap=[]

for i in d['vehicles']:
    scooter_cap.append(d['vehicles'][i]['capacity'])

print("Distance to neighbourhood from restaurant r0 :",res_dist)

print("Order_quantity for each area ",ord_quantity)

print("capacity of scooter :",scooter_cap)

print("Total quantity :",sum(ord_quantity))

