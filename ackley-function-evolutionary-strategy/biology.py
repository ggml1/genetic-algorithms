from individual import Individual
from utils import should_event_happen, gen_random_permutation, generate_random_integer, choose_k_from_array
from recombination import recombination
from parameters import params as CFG
from random import shuffle

NUMBER_OF_PARENTS = 2

def generate_population(population_size):
  return [ Individual() for i in range(population_size) ]

def select_strongest_individual(population):
  return sorted(population)[-1:] 

def best_parents_selection(population):
  return sorted(population) [-2:]

def local_parents_selection(population):
  if (NUMBER_OF_PARENTS > len(population)):
    raise Exception("[ERR - PARENT_SELECTION]: Number of parents must be smaller than the size of the population")
  
  # Subtracts 1 from the indexes generated in the random
  # permutation, due to the 0-indexing used by arrays.
  random_permutation = gen_random_permutation(len(population))
  parent_indexes = random_permutation[:NUMBER_OF_PARENTS]
  return [ population[index] for index in parent_indexes ]

def global_parents_selection(population):
  number_of_parents = generate_random_integer(lower_bound = 2, upper_bound = len(population))
  return choose_k_from_array(population, number_of_parents)

def select_parents(population, parent_selection_strategy = CFG["PRNT_SEL"]):
  if parent_selection_strategy == 'LOCAL':
    return local_parents_selection(population)
  elif parent_selection_strategy == 'GLOBAL':
    return global_parents_selection(population)
  else:
    raise Exception("[ERR - PARENT_SELECTION]: Unknown parent selection strategy")

def generate_offspring(parents):
  child_fenotype, child_sigma = recombination(parents)
  child = Individual(fenotype = child_fenotype, sigma = child_sigma)
  
  if (should_event_happen(CFG["MUT_PRB"])):
    child.mutate()
  
  return child

def kill_suckers(population, children, population_size, survival_strategy = CFG["SRV_STR"]):
  if survival_strategy == "REPLACE_PARENTS":
    # Choose the best children and completely OBLITERATE the parents.
    return sorted(children)[-population_size:]
  elif survival_strategy == "BEST_FIT":
    # Rank all Individuals (parents + children) and Kills the weakest among them,
    # fitness-wise.
    return sorted(population + children)[-population_size:]
  elif survival_strategy == "BALANCED":
    assert(type(population) == type(children) and type(population) == list)
    s = sorted(population + children)
    half = population_size // 2
    best = 25
    worse = 5
    pop = s[:worse] + s[-best:]
    shuffle(pop)
    return pop
  else:
    raise Exception(f"[ERR - SURVIVORS SELECTION] Invalid strategy {survival_strategy}")
