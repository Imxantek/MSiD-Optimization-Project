import sys
import random

size: int
num : int
it : int
evap_rate : float
p_matrix : list[list[float]]


def start_simulation(matrix_size, ant_num, iterations, rate):

    global size, num, it, evap_rate, p_matrix
    size = matrix_size
    num = ant_num
    it = iterations
    evap_rate = rate
    p_matrix = list()

    for i in range(size):
        row = [1.0 for x in range(size)]
        p_matrix.append(row)
    # for i in p_matrix:
    #     print(i)

def p_sum(row: int, avb_locations: set[int]) -> float:
    s = 0.0
    for col in avb_locations:
        s+=p_matrix[row][col]
    return s

def find_index(loc: int, val: float, avb_locations: set[int]) -> int:
    s=0.0
    for i in range(size):
        if i in avb_locations:
            s+=p_matrix[loc][i]
            if s>=val:
                return i

    return list(avb_locations)[0]

def build_permutation() -> list[int]:
    objects_to_assign : list[int] = list(range(size))
    permutation : list[int] = list()
    random.shuffle(objects_to_assign)
    avb_locations: set[int] = set(objects_to_assign)

    for i in range(size):
        permutation.append(-1)

    for loc in objects_to_assign:
        rand=p_sum(loc, avb_locations)*random.random()
        chosen_loc=find_index(loc, rand, avb_locations)
        permutation[loc]=chosen_loc
        avb_locations.remove(chosen_loc)

    return permutation

if __name__ == '__main__':
    start_simulation(3,10,100,0.1)
    print(build_permutation())
