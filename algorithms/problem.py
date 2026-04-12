import math
import sys


n: int
dist_matrix : list[list[int]] = list()
flow_matrix : list[list[int]] = list()
cache={}

# first load dist, then flow

def load_data():
    global n
    global dist_matrix
    global flow_matrix
    flag : bool = True

    n=int(sys.stdin.readline())
    sys.stdin.readline()
    for line in sys.stdin:
        line=line.strip()

        if line=='':
            flag=False
            continue

        line_split=line.split()

        if flag:
            dist_matrix.append([int(x) for x in line_split])

        else:
            flow_matrix.append([int(x) for x in line_split])




# List index -> Object no. (dist)
# List value -> Localisation no. (loc)

def calculate_score(permutation : list[int]) -> int:
    global cache
    sum: int = 0
    perm_tuple=tuple(permutation)
    if perm_tuple in cache:
        return cache[perm_tuple]

    for i in range(len(permutation)):
        obj=i
        loc=permutation[i]

        curr_flow_row=flow_matrix[obj]
        curr_dist_row=dist_matrix[loc]
        for j in range(i+1,len(permutation)):
            target_obj=j
            target_loc=permutation[j]
            dist=curr_flow_row[target_obj]*curr_dist_row[target_loc]
            sum+=dist

    cache[perm_tuple]=sum*2
    return sum*2
