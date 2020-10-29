import random
import numpy as np
from parameters import params as CFG

def check_parents_fenotype_length(parents):
  expected_fenotype_length = len(parents[0].fenotype)
  
  for parent in parents:
    if len(parent.fenotype) != expected_fenotype_length:
      return False
  
  return True

def recombination(parents, recombination_type = CFG["RECOMB_TYPE"]):
  if (not check_parents_fenotype_length(parents)):
    raise Exception("[ERR-RECOMBINATION] Parents' fenotype must have the same length.")

  fenotype = []
  
  for i in range(len(parents[0].fenotype)):
    parents_fenotypes = [ parent.fenotype[i] for parent in parents ]

    if (recombination_type == 'INTERMEDIATE'):
      z_i = np.average(parents_fenotypes)
    elif (recombination_type == 'DISCRETE'):
      z_i = random.choice(parents_fenotypes)
    else:
      raise Exception("[ERR-RECOMBINATION] Unknown recombination type")

    fenotype.append(z_i)

  return np.array(fenotype)
