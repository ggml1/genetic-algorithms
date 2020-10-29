from math import exp, sqrt
from utils import normal_distribution
from parameters import params as CFG

def learning_rate_thao(tao_type = "default"):
  tao = 0
  if tao_type == "default":
    tao = 1 / sqrt(CFG["ACK_N"])
  elif tao_type == "tao_line":
    tao = 1 / sqrt(2 * CFG["ACK_N"])
  elif tao_type == "tao_n_steps":
    tao = 1 / sqrt(2 * sqrt(CFG["ACK_N"]))

  return CFG["LRN_RT_MLT"] * tao


def uncorrelated_mutation(fenotype, sigma ):
  new_sigma = sigma * exp(learning_rate_thao("default") * normal_distribution(0, 1))
  if new_sigma < CFG["EPS_ZRO"]:
    new_sigma = CFG["EPS_ZRO"]
  
  for i in range(len(fenotype)):
    fenotype[i] = fenotype[i] + new_sigma * normal_distribution(0, 1)

  #print("sigma: {}".format(str(new_sigma)))
  return fenotype, new_sigma


def uncorrelated_mutation_n_steps(fenotype, sigmas):
  for i in range(len(sigmas)):
    fixed_normal = normal_distribution(0, 1)
    sigmas[i] = sigmas[i] * exp( (learning_rate_thao("tao_line") * fixed_normal) + learning_rate_thao("tao_n_steps") * normal_distribution(0, 1))

  for i in range(len(fenotype)):
    fenotype[i] = fenotype[i] + sigmas[i] * normal_distribution(0, 1)

  return fenotype, sigmas