import problem
from math import exp
import random

def simulated_annealing(initial_temp, cooling_rate, min_temp) -> tuple[list[int], int]:
    size = problem.n

    current_perm = list(range(size))
    random.shuffle(current_perm)
    current_score = problem.calculate_score(current_perm)

    best_perm = current_perm.copy()
    best_score = current_score

    current_temp = initial_temp

    while current_temp > min_temp:
        new_perm = swap(current_perm)
        new_score = problem.calculate_score(new_perm)

        delta = new_score - current_score

        if delta < 0 or random.random() < exp(-delta / current_temp):
            current_perm = new_perm
            current_score = new_score

            if current_score < best_score:
                best_perm = current_perm.copy()
                best_score = current_score

        current_temp = current_temp * cooling_rate

    return best_perm, best_score


def swap(perm : list[int]) -> list[int]:
    new_perm = perm.copy()
    idx1, idx2 = random.sample(range(len(perm)), 2)
    new_perm[idx1], new_perm[idx2] = new_perm[idx2], new_perm[idx1]
    return new_perm

if __name__ == '__main__':
    problem.load_data()
    best_permutation_result, best_score_result = simulated_annealing(1000.0,0.999,0.1)
    print("Best permutation: ", best_permutation_result)
    print("Best score: ", best_score_result)

