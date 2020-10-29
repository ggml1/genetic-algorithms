import numpy as np
from parameters import params as CFG

def generate_random_double_array(length, lower_bound = CFG["LWR_BND"], upper_bound = CFG["UPR_BND"]):
  return np.random.uniform(low = lower_bound, high = upper_bound, size = (length,))

def normal_distribution(mean, standard_deviation, length = 1):
  return np.random.normal(loc = mean, scale = standard_deviation, size = length)

def should_event_happen(probability):
  return np.random.rand() < probability

def population_average_fitness(population):
  return np.average(list(map(lambda ind: ind.fitness(), population)))

def population_best_fitness(population):
  return np.min(list(map(lambda ind: ind.fitness(), population)))

def population_worst_fitness(population):
  return np.max(list(map(lambda ind: ind.fitness(), population)))

def gen_random_permutation(length):
  return list(map(lambda index : index - 1, np.random.permutation(length)))
