import numpy as np

class Crossover:

  @staticmethod
  def cut_and_crossfill(chromosome_a, chromosome_b):
    chromosome_length = len(chromosome_a)
    cutting_point = np.random.randint(1, chromosome_length - 1)

    chromosome_c = chromosome_a[:cutting_point]
    chromosome_d = chromosome_b[:cutting_point]

    a_index = 0
    b_index = 0

    while len(chromosome_d) != chromosome_length:
        if not chromosome_a[a_index] in chromosome_d:
            chromosome_d = np.append(chromosome_d, chromosome_a[a_index])

        a_index += 1

    while len(chromosome_c) != chromosome_length:
        if not chromosome_b[b_index] in chromosome_c:
            chromosome_c = np.append(chromosome_c, chromosome_b[b_index])

        b_index += 1

    return chromosome_c, chromosome_d
