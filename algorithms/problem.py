import math
import sys


n: int
dist_matrix : list[list[int]] = list()
flow_matrix : list[list[int]] = list()
cache={}
calculate_score = None

# first load dist, then flow

def load_data():
    global n
    global dist_matrix
    global flow_matrix
    flag : bool = True
    global calculate_score

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

    if is_matrix_symmetric(flow_matrix) and is_matrix_symmetric(dist_matrix):
        calculate_score = calculate_score_symmetric
    else:
        calculate_score = calculate_score_asymmetric



# List index -> Object no. (dist)
# List value -> Localisation no. (loc)

def calculate_score_symmetric(permutation : list[int]) -> int:
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


def calculate_score_asymmetric(permutation : list[int]) -> int:
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
        for j in range(len(permutation)):
            target_obj=j
            target_loc=permutation[j]
            dist=curr_flow_row[target_obj]*curr_dist_row[target_loc]
            sum+=dist

    cache[perm_tuple]=sum
    return sum



def is_matrix_symmetric(matrix: list[list[int]]) -> bool:
    for i in range(len(matrix)):
        if matrix[i][i] != 0:
            return False

        for j in range(i + 1, len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True