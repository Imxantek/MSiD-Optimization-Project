import sys
import time
import statistics
import problem
import SA
import ACO

SA_RUNS  = 10
ACO_RUNS = 10
ACO_ANTS = 30
ACO_ITER = 1000
ACO_EVAP = 0.1

# --- SA ---

def run_sa():
    scores, times = [], []
    for _ in range(SA_RUNS):
        t0 = time.perf_counter()
        _, score = SA.simulated_annealing(1000.0, 0.999, 0.1)
        times.append(time.perf_counter() - t0)
        scores.append(score)
    return scores, times

# --- ACO ---

def run_aco():
    scores, times = [], []
    for _ in range(ACO_RUNS):
        ACO.winner = []
        ACO.best_score = sys.maxsize
        t0 = time.perf_counter()
        ACO.start_simulation(problem.n, ACO_ANTS, ACO_ITER, ACO_EVAP)
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
    print(f"    Najlepszy wynik : {best}")
    print(f"    Średni wynik    : {mean:.0f}")
    print(f"    Odch. std       : {std:.1f}  (CV = {cv:.1f}%)")
    print(f"    Czas (średni)   : {t_avg:.2f} s")
    print(f"    Wyniki          : {scores}")

# --- Main ---

if __name__ == "__main__":
    problem.load_data()
    print(f"Problem załadowany: n={problem.n}")

    print("\n=== Symulowane wyżarzanie ===")
    sa_scores, sa_times = run_sa()
    print_stats("SA", sa_scores, sa_times)

    print("\n=== Algorytm mrówkowy ===")
    aco_scores, aco_times = run_aco()
    print_stats("ACO", aco_scores, aco_times)