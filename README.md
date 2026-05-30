# MSiD-Optimization-Project

Project realized as part of the Simulation and Optimization Methods (MSiD) course. The aim of this project is the implementation, analysis, and comparison of the effectiveness of two metaheuristic algorithms: **Simulated Annealing (SA)** and **Ant Colony Optimization (ACO)** applied to the **Quadratic Assignment Problem (QAP)**.

## Project Structure
* `/algorithms` – contains the implementation of the algorithms and the QAP logic:
    * `main.py` – the main script for running tests and collecting statistics.
    * `ACO.py` – implementation of the Ant Colony Optimization algorithm (both standard and elitist versions).
    * `SA.py` – implementation of the Simulated Annealing algorithm.
    * `problem.py` – data parser and objective functions (includes *cache* optimization).
* `/data` – test instances in the QAPLIB format.

## Requirements
* Python 3.x
* Libraries: `statistics`, `time`, `sys`, `random`, `math` (Python standard library).

## Usage
The project is executed using the `main.py` module. The program requires the input data file to be redirected to the standard input.

### Command:
Navigate to the `/algorithms` directory and execute the following command in your terminal:

```bash
python main.py < ../data/FileName.txt
```

**Example:**
```bash
python main.py < ../data/Chr12a.txt
```

## Features
* **Algorithm Comparison:** `main.py` performs a series of runs (default is 10) for each algorithm and generates the following statistics:
    * Best score
    * Average score
    * Standard deviation and coefficient of variation (CV)
    * Average computation time
* **Optimization:** The objective function implementation utilizes a dictionary (cache) to store the results of previously calculated permutations. This drastically speeds up the execution time when dealing with a high number of iterations.
* **ACO Elitism:** The ability to choose between the standard ACO algorithm and an elitist version (which heavily favors the best permutations and historical records).

## Parameters
Algorithm parameters (number of ants, number of iterations, initial temperature, etc.) can be configured directly in the `main.py` file within the following sections:
* `# --- SA PARAMETERS ---`
* `# --- ACO PARAMETERS ---`

## Authors
* Mateusz Cygan (284330)
* Antoni Kamiński (284339)
* Group no. 4, Tuesday P 15:15