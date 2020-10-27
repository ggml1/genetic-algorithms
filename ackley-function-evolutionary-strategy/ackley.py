import numpy as np

ACKLEY_N = 30

def ackley_function(chromosome, C1 = 20.0, C2 = 0.20, C3 = 2.0 * np.pi):
  sum_1 = 0
  sum_2 = 0
  for i in range(ACKLEY_N):
    sum_1 += chromosome[i] * chromosome[i]
    sum_2 +=  np.cos(C3 * chromosome[i])
  sum_1 = sum_1 / ACKLEY_N
  sum_2 = sum_2 / ACKLEY_N
  return -1 * C1 * np.exp(-1 * C2 * np.sqrt(sum_1)) - np.exp(sum_2) + C1 + 1
