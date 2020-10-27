import random
import numpy as np

def recombination(parent_a, parent_b, recombination_type = 'DISCRETE'):
  if (len(parent_a.fenotype) != len(parent_b.fenotype)):
    raise Exception("[ERR-RECOMBINATION] Parents' fenotype must have the same length.")

  fenotype = []

  for i in range(len(parent_a.fenotype)):
    x_i = parent_a.fenotype[i]
    y_i = parent_b.fenotype[i]

    if (recombination_type == 'INTERMEDIATE'):
      z_i = (x_i + y_i) / 2
    elif (recombination_type == 'DISCRETE'):
      z_i = random.choice([x_i, y_i])
    else:
      raise Exception("[ERR-RECOMBINATION] Unknown recombination type")

    fenotype.append(z_i)

  return np.array(fenotype)
