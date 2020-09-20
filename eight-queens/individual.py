import numpy as np
from functools import total_ordering
from queens import ChessBoard

@total_ordering
class Individual(ChessBoard):
  MAXIMUM_FITNESS = 0

  def __init__(self, chromosome = None, chromosome_length = None):
    """
      Initializes an individual.

      If @chromosome is not given, a random one will be generated
      containing @chromosome_length genes.
    """
    if chromosome is None and chromosome_length is None:
      raise Exception('Failed to initialize an individual. One of chromosome and chromosome_length must be passed to the class constructor.')
    
    if chromosome is None:
      chromosome = Individual.generate_random_chromosome(chromosome_length)

    super().__init__(chromosome)
    self.fitness = self.fitness_function()
    self.chromosome = chromosome

  def mutate(self):
    """
      Performs a mutation on this individual's
      chromosome, by choosing a random gene
      and replacing it by another randomly
      generated one.
    """
    chromosome_length = len(self.chromosome)
    new_gene = np.random.randint(0, chromosome_length)
    new_gene_position = np.random.randint(0, chromosome_length)
    self.chromosome[new_gene_position] = new_gene
    
  def fitness_function(self):
    """
      This function calculates the fitness of
      a given individual. Since an individual
      is a representation of a N-queens placement
      on the chess board, we can evaluate the
      function as follows:

      -> The fitness increases inversely proportional
        to the number of collisions generated by the
        individual's placement of queens.
    """
    return -1 * self.get_number_of_collisions() # Fewer collisions should represent higher fitness
  
  def __lt__(self, other):
    return self.fitness < other.fitness
  
  def __eq__(self, other):
    return self.fitness == other.fitness

  @staticmethod
  def generate_random_chromosome(length):
    chromosome = np.arange(length)
    np.random.shuffle(chromosome)
    return chromosome
