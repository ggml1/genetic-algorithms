from biology import *
from utils import pop_best_fitness, pop_worst_fitness, pop_avg_fitness, pop_std_fitness, pop_avg_mut_step
import matplotlib.pyplot as plt
import logging
from datetime import datetime
from parameters import params as CFG

# logging.basicConfig(filename="evol_strategy_run_{}.log".format(datetime.now().strftime("%d-%m-%Y-%H-%M-%SS")), level=logging.INFO)

def main(number_of_iterations = CFG["ITR_AMT"],
         population_size = CFG["POP_SIZE"],
         parent_couples_per_iteration = CFG["PRT_CPL"],
         children_amount_per_parent_pair= CFG["CHL_PPR"]):

  print("EVOLUTIONARY ALGORITHM PARAMETERS: {}".format(str(CFG)))

  population = generate_population(population_size)

  for iteration in range(number_of_iterations):
    #sca = plt.scatter(iteration, population_average_fitness(population), s=200, lw=0, c='red', alpha=0.5); plt.pause(0.05)

    #print("Iteration: {} - AVG Fitness: {} - Best Fitness: {} - Worst Fitness {}".format(str(iteration), population_average_fitness(population), population_best_fitness(population), population_worst_fitness(population)))
    iteration_statistics = "\"{}\": {{ \"best_fitness\":{},  \"worst_fitness\":{}, \"avg_fitness\":{}, \"std_dev_fitness\":{}, \"avg_mutation_step\":{} }}".format(str(iteration),
                                                                                                                                                                        pop_best_fitness(population),
                                                                                                                                                                        pop_worst_fitness(population),
                                                                                                                                                                        pop_avg_fitness(population),
                                                                                                                                                                        pop_std_fitness(population),
                                                                                                                                                                        pop_avg_mut_step(population)
                                                                                                                                                                        )
    print(iteration_statistics)
    # logging.info(iteration_statistics)

    children = []
    for i in range(parent_couples_per_iteration):
      parents = select_parents(population)
      for j in range(children_amount_per_parent_pair):
        child = generate_offspring(parents)
        children.append(child)
        # print("GENERATED CHILD: {}".format(str(child)))
        
    population = kill_suckers(population, children, population_size)
  
  #plt.ioff(); plt.show()

  return

if __name__ == '__main__':
  main()
