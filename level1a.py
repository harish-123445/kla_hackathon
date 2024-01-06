import json
f = open('kla_hackathon/Student_Handout/Input_data/level1a.json')
d = json.load(f)
neighbour=d['neighbourhoods']
#let us define two lists to hold order quantity and distances
ord_quantity=[]
distance=[]
for i in neighbour.keys():
    temp=list(neighbour[i].values())
    ord_quantity.append(temp[0])
    distance.append(temp[1])
st_pt='r0'
res=d['restaurants']
distance.insert(0,(res['r0'])['neighbourhood_distance'])
distance[0].insert(0,0)  
for i in range(1,21):
    distance[i].insert(0,distance[0][i])

print(ord_quantity)


scooter_cap=d['vehicles']['v0']['capacity']
print(scooter_cap)

#knapsack loading problem

