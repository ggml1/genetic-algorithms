import numpy as np
from queens import ChessBoard
from crossover import Crossover
from individual import Individual

def should_event_happen(probability):
  """
    Returns true or false - whether an event
    should happen or not, given the probability
    of its occurrence.

    This is mainly used to define when mutations
    and recombinations will occur.
  """
  return np.random.rand() < probability

def generate_child(parent_a, parent_b, mutation_probability):
  child_a_chromosome, child_b_chromosome = Crossover.cut_and_crossfill(parent_a.chromosome, parent_b.chromosome)
  child_a = Individual(chromosome = child_a_chromosome)
  child_b = Individual(chromosome = child_b_chromosome)

  if should_event_happen(mutation_probability):
    child_a.mutate()

  if should_event_happen(mutation_probability):
    child_b.mutate()

  return child_a, child_b

def generate_offspring(parent_a, parent_b, recombination_probability, mutation_probability):
  # In case recombination does not occur, parents will reproduce themselves.
  children = [parent_a, parent_b]

  if should_event_happen(recombination_probability):
    child_a, child_b = generate_child(parent_a, parent_b, mutation_probability)
    children = [child_a, child_b]

  return children

def get_random_population(number_of_individuals, number_of_queens):
    return [ Individual(chromosome_length = number_of_queens) for count in range(number_of_individuals) ]

def generate_population(number_of_individuals, number_of_queens):
  while True:
      population = get_random_population(number_of_individuals, number_of_queens)

      has_maximum_fitness_individual = False
      for individual in population:
          if individual.fitness == individual.MAXIMUM_FITNESS:
              has_maximum_fitness_individual = True

      if not has_maximum_fitness_individual:
          # We do not want a starting set that
          # already solves our problem.
          return population
