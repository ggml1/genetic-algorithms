from math import exp, sqrt
from ackley import ACKLEY_N
from utils import normal_distribution

EPSILON_ZERO = 0.01

def uncorrelated_mutation(fenotype, sigma, tao = 1 / sqrt(ACKLEY_N)):
  new_sigma = sigma * exp(tao * normal_distribution(0, 1))
  if new_sigma < EPSILON_ZERO:
    new_sigma = EPSILON_ZERO
  
  for i in range(len(fenotype)):
    fenotype[i] = fenotype[i] + new_sigma * normal_distribution(0, 1)

  #print("sigma: {}".format(str(new_sigma)))
  return fenotype, new_sigma


def uncorrelated_mutation_n_steps(fenotype, sigmas, tao_line = 1 / sqrt(2 * ACKLEY_N), tao = 1 / sqrt(2 * sqrt(ACKLEY_N))):
  for i in range(len(sigmas)):
    fixed_normal = normal_distribution(0, 1)
    sigmas[i] = sigmas[i] * exp( (tao_line * fixed_normal) + tao * normal_distribution(0, 1))

  for i in range(len(fenotype)):
    fenotype[i] = fenotype[i] + sigmas[i] * normal_distribution(0, 1)

  return fenotype, sigmas