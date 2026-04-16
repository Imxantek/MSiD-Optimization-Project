import sys
import random
import problem
problem.load_data()

size: int
num : int
it : int
evap_rate : float
p_matrix : list[list[float]]
winner: list[int] = list()
best_score : int = sys.maxsize
retention_rate: float = 1.0

def start_simulation(matrix_size, ant_num, iterations, rate):

    global size, num, it, evap_rate, p_matrix, retention_rate
    size = matrix_size
    num = ant_num
    it = iterations
    evap_rate = rate
    p_matrix = list()
    retention_rate = 1.0-evap_rate

    for i in range(size):
        row = [1.0 for x in range(size)]
        p_matrix.append(row)
    # for i in p_matrix:
    #     print(i)

def find_idx(row: int, avb_locations: set[int]) -> int:
    s=0.0
    val=random.random()
    for i in avb_locations:
        s+=p_matrix[row][i]

    val*=s
    s=0

    for i in avb_locations:
       s+=p_matrix[row][i]
       if s>=val:
           return i

    return next(iter(avb_locations))



def build_permutation() -> list[int]:
    objects_to_assign : list[int] = list(range(size))
    permutation : list[int] = list()
    random.shuffle(objects_to_assign)
    avb_locations: set[int] = set(objects_to_assign)

    permutation = [-1] * size

    for row in objects_to_assign:
        chosen_loc=find_idx(row, avb_locations)
        permutation[row]=chosen_loc
        avb_locations.remove(chosen_loc)

    return permutation

def simulate():
    global winner, best_score
    permutations : list[tuple[list[int], int]] = list()

    for i in range(num):
        current = build_permutation()
        score = problem.calculate_score(current)
        permutations.append((current, score))

        if score < best_score:
            best_score = score
            winner = current

        # print("current: ", current, " score: ", score)

    for i in range(size):
        for j in range(size):
            p_matrix[i][j]*=retention_rate

    for tup in permutations:
        perm=tup[0]
        score=tup[1]

        for i in range(len(perm)):
            p_matrix[i][perm[i]]+=best_score/score

    # print("Pheromones Matrix: ")
    # for row in p_matrix:
    #     print(row)

def run_simulation():
    for i in range(it):
        simulate()

if __name__ == '__main__':
    start_simulation(problem.n,12,35000,0.1)
    run_simulation()
    print("Best permutation: ")
    print(winner)
    print("Score: ")
    print(best_score)