import numpy as np
import random
from parameters import params as CFG

def generate_random_double_array(length, lower_bound = CFG["LWR_BND"], upper_bound = CFG["UPR_BND"]):
  return np.random.uniform(low = lower_bound, high = upper_bound, size = (length,)).tolist()

def normal_distribution(mean, standard_deviation, length = 1):
  return np.random.normal(loc = mean, scale = standard_deviation, size = length)[0]

def should_event_happen(probability):
  return np.random.rand() < probability

def pop_avg_fitness(population):
  return np.average(list(map(lambda ind: ind.fitness(), population)))

def pop_best_fitness(population):
  return np.min(list(map(lambda ind: ind.fitness(), population)))

def pop_worst_fitness(population):
  return np.max(list(map(lambda ind: ind.fitness(), population)))

def pop_std_fitness(population):
  return np.std(list(map(lambda ind: ind.fitness(), population)))

def pop_avg_mut_step(population):
  avg = 0
  if CFG["MUT_TYP"] == "UNCORRELATED_SINGLE":
    avg = np.average(list(map(lambda ind: ind.sigma[0], population)))
  elif CFG["MUT_TYP"] == "UNCORRELATED_MANY":
    avg = np.average(list(map(lambda ind: np.average(ind.sigma), population)))
  return avg

def gen_random_permutation(length):
  return list(map(lambda index : index - 1, np.random.permutation(length)))

def generate_random_integer(lower_bound = 2, upper_bound = CFG["POP_SIZE"]):
  return np.random.randint(low = lower_bound, high = upper_bound)

def choose_k_from_array(array, k):
  return random.sample(array, k)
