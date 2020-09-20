import numpy as np
from queens import ChessBoard
from crossover import Crossover
from individual import Individual

def will_mutate(probability):
  """
    Returns True or False - whether the mutation
    will occur, according to a given
    probability of it occurring or not.
    
    Example: if the given probability is 0.4 (40%), the
    mutation will occur if a randomly chosen float is
    less than or equal to 0.4.
  """
  return np.random.rand() < probability

def will_recombine(probability):
  """
    Returns True or False - whether the recombination
    will occur, according to a given
    probability of it occurring or not.
    
    Example: if the given probability is 0.4 (40%), the
    recombination will occur if a randomly chosen float is
    less than or equal to 0.4.
  """
  return np.random.rand() < probability

def generate_child(parent_a, parent_b, mutation_probability):
  child_chromosome = Crossover.cut_and_crossfill(parent_a.chromosome, parent_b.chromosome)
  child = Individual(chromosome = child_chromosome)
  
  if will_mutate(mutation_probability):
    child.mutate()

  return child

def generate_offspring(parent_a, parent_b, recombination_probability, mutation_probability):
  # In case recombination does not occur, parents will reproduce themselves.
  children = [parent_a, parent_b]

  if will_recombine(recombination_probability):
    child_a = generate_child(parent_a, parent_b, mutation_probability)
    child_b = generate_child(parent_b, parent_a, mutation_probability)
    children = [child_a, child_b]

  return children

def generate_population(number_of_individuals, number_of_queens):
  return [ Individual(chromosome_length = number_of_queens) for count in range(number_of_individuals) ]
