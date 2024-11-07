import random

# Constants
NUM_QUEENS = 8
MUTATION_RATE = 0.2
GENERATIONS = 1000

# Initialize a single random individual (one solution candidate)
def initialize_individual():
    return [random.randint(0, NUM_QUEENS - 1) for _ in range(NUM_QUEENS)]

# Calculate fitness as the number of non-attacking pairs of queens
def fitness_function(individual):
    non_attacking_pairs = 0
    for i in range(NUM_QUEENS):
        for j in range(i + 1, NUM_QUEENS):
            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != j - i:
                non_attacking_pairs += 1
    return non_attacking_pairs

# Perform crossover by mixing parts of two individuals
def crossover(parent1, parent2):
    crossover_point = random.randint(0, NUM_QUEENS - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# Mutate an individual by changing the position of a queen with some probability
def mutate(individual):
    if random.random() < MUTATION_RATE:
        index = random.randint(0, NUM_QUEENS - 1)
        individual[index] = random.randint(0, NUM_QUEENS - 1)
    return individual

# Genetic Algorithm for finding a solution to the 8-Queens problem
def genetic_algorithm():
    current_individual = initialize_individual()
    best_fitness = fitness_function(current_individual)
    
    for generation in range(GENERATIONS):
        if best_fitness == (NUM_QUEENS * (NUM_QUEENS - 1)) // 2:
            break  # Solution found
        
        # Generate a new individual by crossover with a mutated version of itself
        new_individual = mutate(crossover(current_individual, initialize_individual()))
        new_fitness = fitness_function(new_individual)
        
        # If the new individual is better, update the best individual
        if new_fitness > best_fitness:
            current_individual = new_individual
            best_fitness = new_fitness
    
    return current_individual

# Run the algorithm and print the best solution
best_solution = genetic_algorithm()
print("Best solution:", best_solution)
print("Fitness:", fitness_function(best_solution))
