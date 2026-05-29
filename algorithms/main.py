import sys
import time
import statistics
import problem
import SA
import ACO

# --- SA PARAMETERS ---
SA_RUNS  = 10
SA_TEMP = 1000.0
SA_COOL_RATE = 0.999
SA_MIN_TEMP = 0.1

# --- ACO PARAMETERS ---
ACO_RUNS = 10
ACO_ANTS = 60
ACO_ITER = 100
ACO_EVAP = 0.1
ELITIST=True

# --- SA ---

def run_sa():
    scores, times = [], []
    for _ in range(SA_RUNS):
        problem.cache = {}
        t0 = time.perf_counter()
        _, score = SA.simulated_annealing(SA_TEMP, SA_COOL_RATE, SA_MIN_TEMP)
        times.append(time.perf_counter() - t0)
        scores.append(score)
    return scores, times

# --- ACO ---

def run_aco():
    scores, times = [], []
    for _ in range(ACO_RUNS):
        problem.cache = {}
        ACO.winner = []
        ACO.best_score = sys.maxsize
        t0 = time.perf_counter()
        ACO.start_simulation(problem.n, ACO_ANTS, ACO_ITER, ACO_EVAP, ELITIST)
        ACO.run_simulation()
        times.append(time.perf_counter() - t0)
        scores.append(ACO.best_score)
    return scores, times

# --- Statystyki ---

def print_stats(name, scores, times):
    best  = min(scores)
    mean  = statistics.mean(scores)
    std   = statistics.stdev(scores) if len(scores) > 1 else 0.0
    cv    = std / mean * 100 if mean else 0.0
    t_avg = statistics.mean(times)

    print(f"\n  {name}")
    print(f"    Best score : {best}")
    print(f"    Average score    : {mean:.0f}")
    print(f"    Std. deviation       : {std:.1f}  (CV = {cv:.1f}%)")
    print(f"    Time (average)   : {t_avg:.2f} s")
    print(f"    Scores          : {scores}")

# --- Main ---

if __name__ == "__main__":
    problem.load_data()
    print(f"Problem loaded: n={problem.n}")

    print("\n=== Simulated Annealing ===")
    print(f"  runs={SA_RUNS}, temp={SA_TEMP}, cooling_rate={SA_COOL_RATE}, min_temp={SA_MIN_TEMP}")
    sa_scores, sa_times = run_sa()
    print_stats("SA", sa_scores, sa_times)

    print("\n=== Ant Colony Optimization ===")
    print(f"  runs={ACO_RUNS}, ants={ACO_ANTS}, iterations={ACO_ITER}, evap_rate={ACO_EVAP}")
    aco_scores, aco_times = run_aco()
    print_stats("ACO", aco_scores, aco_times)