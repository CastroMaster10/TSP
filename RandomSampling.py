import numpy as np
import time
import random
from itertools import permutations

def calculate_total_distance(path, distance_matrix):
    total_path_distance = 0
    for i in range(len(path) - 1):
        current_city = path[i]
        next_city = path[i + 1]
        total_path_distance += distance_matrix[current_city][next_city]
    return total_path_distance

def solve_salesman_problem(distance_matrix):
    number_of_cities = len(distance_matrix)
    city_list = list(range(number_of_cities))
    best_path = None
    best_distance = float('inf')
    total_operations = 0
    start_time = time.time()
    all_permutations = list(permutations(city_list[1:], number_of_cities - 1))
    number_of_permutations_to_choose = 200
    random_permutations = random.sample(all_permutations, number_of_permutations_to_choose)
    for perm in random_permutations:
        path = [0] + list(perm) + [0]
        path_distance = calculate_total_distance(path, distance_matrix)
        total_operations += 1
        if path_distance < best_distance:
            best_distance = path_distance
            best_path = path
    end_time = time.time()
    execution_time = end_time - start_time
    return best_path, best_distance, total_operations, execution_time

# Distance matrix
distance_matrix = np.array([
    [999, 12, 10, 999, 999, 999, 12],
    [12, 999, 8, 12, 999, 999, 999],
    [10, 8, 999, 11, 3, 999, 9],
    [999, 12, 11, 999, 11, 10, 999],
    [999, 999, 3, 11, 999, 6, 7],
    [999, 999, 999, 10, 6, 999, 9],
    [12, 999, 9, 999, 7, 9, 999]
])

# Get the path, total distance, total operations, and execution time
acceptable_path, total_distance_traveled, total_operations_performed, total_execution_time = solve_salesman_problem(distance_matrix)

# Print results
print("Acceptable path:", [x + 1 for x in acceptable_path])
print("Total distance traveled:", total_distance_traveled)
print("Total operations performed:", total_operations_performed)
print("Execution time:", total_execution_time, "seconds")