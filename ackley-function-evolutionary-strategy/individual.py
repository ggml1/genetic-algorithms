from ackley import ACKLEY_N, ackley_function
from utils import generate_random_double_array
from mutate import uncorrelated_mutation, uncorrelated_mutation_n_steps

class Individual:
  def __init__(self, fenotype = None, sigma = [1] * ACKLEY_N, length = ACKLEY_N):
    if (fenotype is None):
      fenotype = generate_random_double_array(length)
    
    self.fenotype = fenotype
    self.sigma = sigma
    self._fitness = None

  def fitness(self):
    if (self._fitness is not None):
      return self._fitness

    self._fitness = abs(ackley_function(self.fenotype))
    return self._fitness

  def mutate(self, mutation_function = uncorrelated_mutation):
    self._fitness = None
    if mutation_function == uncorrelated_mutation:
      self.fenotype, self.sigma[0] = mutation_function(self.fenotype, self.sigma[0])
    elif mutation_function == uncorrelated_mutation_n_steps:
      self.fenotype, self.sigma = mutation_function(self.fenotype, self.sigma)

  def __repr__(self):
    return str(self.fenotype)

  def __lt__(self, other):
    return self.fitness() > other.fitness()

  def __eq__(self, other):
    return self.fitness() == other.fitness()
