from biology import *
from utils import population_average_fitness, population_best_fitness, population_worst_fitness
import matplotlib.pyplot as plt
from parameters import params as CFG

def main(number_of_iterations = CFG["ITR_AMT"], population_size = CFG["POP_SIZE"], parent_couples_per_iteration = CFG["PRT_CPL"], children_amount_per_parent_pair= CFG["CHL_PPR"]):
  population = generate_population(population_size)
  
  for iteration in range(number_of_iterations):
    #sca = plt.scatter(iteration, population_average_fitness(population), s=200, lw=0, c='red', alpha=0.5); plt.pause(0.05)

    #print("Iteration: {} - AVG Fitness: {} - Best Fitness: {} - Worst Fitness {}".format(str(iteration), population_average_fitness(population), population_best_fitness(population), population_worst_fitness(population)))
    print("Iteration: {} - Best Fitness: {} - Worst Fitness {}".format(str(iteration), population_best_fitness(population), population_worst_fitness(population)))

    children = []
    for i in range(parent_couples_per_iteration):
      parents = local_parents_selection(population)
      for i in range(children_amount_per_parent_pair):
        child = generate_offspring(parents)
        children.append(child)
        # print("GENERATED CHILD: {}".format(str(child)))
        
    population = kill_suckers(population, children, population_size, CFG["SRV_STR"])
  
  #plt.ioff(); plt.show()

  return

if __name__ == '__main__':
  main()
