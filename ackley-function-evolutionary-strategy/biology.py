from individual import Individual
from utils import should_event_happen, gen_random_permutation
from recombination import recombination
from parameters import params as CFG

NUMBER_OF_PARENTS = 2

def generate_population(population_size):
  return [ Individual() ] * population_size

def select_strongest_individual(population):
  return sorted(population)[-1:] 

def local_parents_selection(population):
  if (NUMBER_OF_PARENTS > len(population)):
    raise Exception("[ERR - PARENT_SELECTION]: Number of parents must be smaller than the size of the population")
  
  # Subtracts 1 from the indexes generated in the random
  # permutation, due to the 0-indexing used by arrays.
  random_permutation = gen_random_permutation(len(population))
  parent_indexes = random_permutation[:NUMBER_OF_PARENTS]
  return [ population[index] for index in parent_indexes ]

def generate_offspring(parents):
  parent_a, parent_b = parents
  child_fenotype = recombination(parent_a, parent_b, recombination_type = 'INTERMEDIATE')
  child = Individual(fenotype = child_fenotype)
  
  if (should_event_happen(CFG["MUT_PRB"])):
    child.mutate()
  
  return child

def kill_suckers(population, children, population_size, survival_strategy = "REPLACE_PARENTS"):
  if survival_strategy == "REPLACE_PARENTS":
    # Choose the best children and completely OBLITERATE the parents.
    return sorted(children)[-population_size:]
  elif survival_strategy == "BEST_FIT":
    # Rank all Individuals (parents + children) and Kills the weakest among them,
    # fitness-wise.
    return sorted(population + children)[-population_size:]
