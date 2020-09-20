import numpy as np
from biology import generate_offspring

def choose_parents(population, number_of_sample_parents):
  """
    Selects two individuals with the highest fitness
    among a sample of @number_of_sample_parents individuals
    extracted from the population.
  """
  sample = np.random.choice(population, size = number_of_sample_parents, replace = False)
  return sorted(sample)[-2:]

def choose_best_individual(population):
  return sorted(population)[-1]

def stop_algorithm(population, iteration_count, max_fitness_evaluations):
  """
    This function returns whether the genetic algorithm should stop.
    The stop point is when one of the individuals in the population
    has reached maximum fitness or the iteration count has reached
    its limit.
  """
  if iteration_count == max_fitness_evaluations:
    return True
  
  for individual in population:
    if individual.fitness == individual.MAXIMUM_FITNESS:
      return True
  
  return False

def genetic_algorithm(population, recombination_probability, mutation_probability, number_of_sample_parents):
  parent_a, parent_b = choose_parents(population, number_of_sample_parents)
  children = generate_offspring(parent_a, parent_b, recombination_probability, mutation_probability)

  for child in children:
    # Adding the newly born children to the population
    population.append(child)

  # We sort the population in ascending-fitness order
  population = sorted(population)

  for count in range(len(children)):
    # For each child added, we remove the weakest children that exists
    # in the population. This is done after children addition because
    # one of them may be part of the population's weakest.
    population.pop(0)

  return population
