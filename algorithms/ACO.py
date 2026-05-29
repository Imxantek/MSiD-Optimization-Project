import sys
import random
import problem

size: int
num : int
it : int
evap_rate : float
p_matrix : list[list[float]]
winner: list[int] = list()
best_score : int = sys.maxsize
retention_rate: float = 1.0
elitist: bool = False

def start_simulation(matrix_size, ant_num, iterations, rate, elitism=False):
    global size, num, it, evap_rate, p_matrix, retention_rate, elitist
    size = matrix_size
    num = ant_num
    it = iterations
    evap_rate = rate
    p_matrix = list()
    retention_rate = 1.0-evap_rate
    elitist = elitism

    for i in range(size):
        row = [1.0 for _ in range(size)]
        p_matrix.append(row)

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
    global winner, best_score, elitist
    permutations : list[tuple[list[int], int]] = list()

    for i in range(num):
        current = build_permutation()
        score = problem.calculate_score(current)
        permutations.append((current, score))

        if score < best_score:
            best_score = score
            winner = current

    for i in range(size):
        for j in range(size):
            p_matrix[i][j]*=retention_rate

    if elitist:
        elitist_simulation(permutations)
    else:
        standard_simulation(permutations)

def elitist_simulation(permutations: list[tuple[list[int], int]]):
    permutations = sorted(permutations, key=lambda x: x[1])
    rewards = [1.5, 0.66, 0.33]
    for i in range(3):
        perm = permutations[i][0]

        for j in range(len(perm)):
            p_matrix[j][perm[j]] += rewards[i]

    for i in range(len(winner)):
        p_matrix[i][winner[i]]+=1.0

def standard_simulation(permutations: list[tuple[list[int], int]]):
    for tup in permutations:
        perm=tup[0]
        score=tup[1]

        for i in range(len(perm)):
            p_matrix[i][perm[i]]+=best_score/score

def run_simulation():
    for i in range(it):
        simulate()