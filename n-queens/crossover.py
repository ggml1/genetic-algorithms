import numpy as np

class Crossover:

  @staticmethod
  def cut_and_crossfill(chromosome_a, chromosome_b):
    chromosome_length = len(chromosome_a)
    cutting_point = np.random.randint(1, chromosome_length - 1)

    chromosome_c = np.append(chromosome_a[:cutting_point], chromosome_b[cutting_point:])

    return chromosome_c
