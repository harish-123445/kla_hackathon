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

print("minimum number of slots :",sum(ord_quantity)/sum(scooter_cap))

scooter_cap.sort(reverse=True)
c=0
current_scooter=scooter_cap[c]

def nearest_neighbor(distance_matrix, ord_quantity):
    c = 0  # Initialize the variable 'c'
    unvisited = set(range(len(distance_matrix)))
    current_node = 0  
    current_capacity = 0
    current_distance = 0
    slots = []
    current_slot=[]
    global current_scooter
    while unvisited:
        unvisited.remove(current_node)
        if current_capacity + ord_quantity[current_node] <=current_scooter :
            current_capacity += ord_quantity[current_node]
            current_slot.append(current_node)
        else:
            slots.append((current_slot, current_distance,c))
            current_slot = [current_node]
            current_capacity = ord_quantity[current_node]
            current_distance = 0
            c+=1
            if (c>4):
                c=0
            current_scooter=scooter_cap[c]

        if unvisited:
            next_node = min(unvisited, key=lambda x: distance_matrix[current_node][x])
            current_distance += distance_matrix[current_node][next_node]
            current_node = next_node

    if current_slot:
        slots.append((current_slot, current_distance))

    return slots

slots = nearest_neighbor(distance, ord_quantity)
print(slots)
final_lst=[]
for i in slots:
    temp=[]
    temp.append('r0')
    for j in i[0]:
        temp.append('n'+str(j))
    temp.append('r0')
    final_lst.append(temp)
print(final_lst)

final_paths={"v0": {"path1": final_lst[0], "path2": final_lst[5]}, "v1": {"path1": final_lst[1], "path2":final_lst[6]}, "v2": {"path1": final_lst[2]},'v3':{"path1": final_lst[3]},'v4':{"path1": final_lst[4]}}

save_file = open("kla_hackathon/my_output/level2a_output.json", "w")  
json.dump(final_paths, save_file, indent = 6)  
save_file.close()