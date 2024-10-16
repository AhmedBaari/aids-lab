import numpy as np

# Parameters
POP_SIZE = 10  # Number of individuals in the population
GENOME_LEN = 10  # Length of each individual's genome
GENERATIONS = 20  # Number of generations to evolve
MUTATION_RATE = 0.01  # Probability of mutation

# Initialize Population: Create random binary population
def initialize_population(size, length):
    return np.random.randint(2, size=(size, length))

# Fitness Function: Sum of the genome (maximize 1s)
def fitness(individual):
    return np.sum(individual)

# Selection Function: Choose parents based on fitness
def select_parents(population, fitness_scores):
    probabilities = fitness_scores / fitness_scores.sum()
    selected_indices = np.random.choice(len(population), size=len(population), p=probabilities)
    return population[selected_indices]

# Crossover Function: Swap parts of two parents to create children
def crossover(parent1, parent2):
    point = np.random.randint(1, len(parent1))
    return np.concatenate((parent1[:point], parent2[point:])), np.concatenate((parent2[:point], parent1[point:]))

# Mutation Function: Flip bits in the genome with a small probability
def mutate(individual, rate):
    mutation = np.random.rand(len(individual)) < rate
    
    individual[mutation] = 1 - individual[mutation]
    return individual

# Genetic Algorithm: Main loop for evolving the population
def genetic_algorithm():
    population = initialize_population(POP_SIZE, GENOME_LEN)
    
    for _ in range(GENERATIONS):
        fitness_scores = np.array([fitness(ind) for ind in population])
        parents = select_parents(population, fitness_scores)
        
        new_population = []
        for i in range(0, POP_SIZE, 2):
            child1, child2 = crossover(parents[i], parents[i+1])
            new_population.append(mutate(child1, MUTATION_RATE))
            new_population.append(mutate(child2, MUTATION_RATE))
        
        population = np.array(new_population)
        best_fitness = max(fitness_scores)
        print(f"Best Fitness: {best_fitness}")
    
    best_individual = population[np.argmax([fitness(ind) for ind in population])]
    return best_individual

# Run the genetic algorithm
best_individual = genetic_algorithm()
print("Best Individual: ", best_individual)
print("Best Fitness: ", fitness(best_individual))
