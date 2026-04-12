import math
import sys


n: int
dist_matrix : list[list[int]] = list()
flow_matrix : list[list[int]] = list()


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

def calculate_cost(permutation : list[int]) -> int:
    sum: int = 0

    for i in range(len(permutation)):
        obj=i
        loc=permutation[i]

        for j in range(i+1,len(permutation)):
            target_obj=j
            target_loc=permutation[j]
            dist=flow_matrix[obj][target_obj]*dist_matrix[loc][target_loc]
            sum+=dist

    return sum*2
