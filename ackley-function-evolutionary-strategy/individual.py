from ackley import ackley_function
from utils import generate_random_double_array
from mutate import uncorrelated_mutation, uncorrelated_mutation_n_steps
from parameters import params as CFG

class Individual:
  def __init__(self, fenotype = None, sigma = [CFG["MUT_STP"]] * CFG["ACK_N"], length = CFG["ACK_N"]):
    if (fenotype is None):
      fenotype = generate_random_double_array(length)
    
    self.fenotype = fenotype
    self.sigma = sigma
    self._fitness = None

  def fitness(self, f = ackley_function):
    if (self._fitness is not None):
      return abs(self._fitness)

    self._fitness = f(self.fenotype)
    return abs(self._fitness)

  def mutate(self, mutation_type = CFG["MUT_TYP"]):
    self._fitness = None
    if mutation_type == "UNCORRELATED_SINGLE":
      self.fenotype, self.sigma[0] = uncorrelated_mutation(self.fenotype, self.sigma[0])
    elif mutation_type == "UNCORRELATED_MANY":
      self.fenotype, self.sigma = uncorrelated_mutation_n_steps(self.fenotype, self.sigma)

  def __repr__(self):
    return str(self.fenotype)

  def __lt__(self, other):
    return self.fitness() > other.fitness()

  def __eq__(self, other):
    return self.fitness() == other.fitness()
