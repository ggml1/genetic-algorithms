import numpy as np
import random
import matplotlib.pyplot as plt
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

def pop_std_dev_mut_step(population):
  std_dev = 0
  if CFG["MUT_TYP"] == "UNCORRELATED_SINGLE":
    std_dev = np.std(list(map(lambda ind: ind.sigma[0], population)))
  elif CFG["MUT_TYP"] == "UNCORRELATED_MANY":
    std_dev = np.std(list(map(lambda ind: np.std(ind.sigma), population)))
  return std_dev

def gen_random_permutation(length):
  return list(map(lambda index : index - 1, np.random.permutation(length)))

def generate_random_integer(lower_bound = 2, upper_bound = CFG["POP_SIZE"]):
  return np.random.randint(low = lower_bound, high = upper_bound)

def choose_k_from_array(array, k):
  return random.sample(array, k)

def get_population_statistics(population):
  return {
    'best_fitness': pop_best_fitness(population),
    'worst_fitness': pop_worst_fitness(population),
    'avg_fitness': pop_avg_fitness(population),
    'std_dev_fitness': pop_std_fitness(population),
    'avg_mutation_step': pop_avg_mut_step(population),
    'std_dev_mutation_step': pop_std_dev_mut_step(population)
  }

def plot_array(y, title = 'Untitled Plot', x_label = None, y_label = None):
  x = [ i + 1 for i in range(len(y)) ]

  fig, ax = plt.subplots()
  ax.plot(x, y)
  ax.set_title(title)
  
  if (x_label):
    ax.set_xlabel(x_label)
  
  if (y_label):
    ax.set_ylabel(y_label)

  fig.savefig(f'{title}.png')
