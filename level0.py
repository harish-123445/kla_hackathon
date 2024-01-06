import json
import numpy as np
f = open('kla_hackathon/Student_Handout/Input_data/level0.json')
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

final_lst=[]

#travelling salesman code
def travellingsalesman(c):
    global cost
    adj_vertex = 5000
    min_val = 5000
    visited[c] = 1
    final_lst.append(c+1)
    #print((c + 1), end=" ")
    for k in range(n):
        if (tsp_g[c][k] != 0) and (visited[k] == 0):
            if tsp_g[c][k] < min_val:
                min_val = tsp_g[c][k]
                adj_vertex = k
    if min_val != 5000:
        cost = cost + min_val
    if adj_vertex == 5000:
        adj_vertex = 0
        final_lst.append(adj_vertex+1)
        #print((adj_vertex + 1), end=" ")
        cost = cost + tsp_g[c][adj_vertex]
        return
    travellingsalesman(adj_vertex)

n = 21
cost = 0
visited = np.zeros(n, dtype=int)
tsp_g = np.array(distance)
travellingsalesman(0)
path=[]
for i in final_lst[1:21]:
    path.append('n'+str(i-2))
path.insert(0,'r0')
path.append('r0')
print(path)
print("total_cost : ",cost)

final_path={"v0": {"path": path}}

save_file = open("my_output/output_level0.json", "w")  
json.dump(final_path, save_file, indent = 6)  
save_file.close()  



