from biology import *
from utils import get_population_statistics, plot_array
import matplotlib.pyplot as plt
import logging
from datetime import datetime
from parameters import params as CFG

logging.basicConfig(filename="evol_strategy_run_{}.log".format(datetime.now().strftime("%d-%m-%Y-%H-%M-%SS")), level=logging.INFO)

def main(number_of_iterations = CFG["ITR_AMT"],
         population_size = CFG["POP_SIZE"],
         parent_couples_per_iteration = CFG["PRT_CPL"],
         children_amount_per_parent_pair= CFG["CHL_PPR"]):

  print("EVOLUTIONARY ALGORITHM PARAMETERS: {}".format(str(CFG)))

  population = generate_population(population_size)

  avg_fitnesses = []
  std_dev_fitnesses = []
  avg_mutation_steps = []
  std_dev_mutation_steps = []

  for iteration in range(number_of_iterations):
    #sca = plt.scatter(iteration, population_average_fitness(population), s=200, lw=0, c='red', alpha=0.5); plt.pause(0.05)

    pop_statistics = get_population_statistics(population)

    avg_fitnesses.append(pop_statistics['avg_fitness'])
    std_dev_fitnesses.append(pop_statistics['std_dev_fitness'])
    avg_mutation_steps.append(pop_statistics['avg_mutation_step'])
    std_dev_mutation_steps.append(pop_statistics['std_dev_mutation_step'])

    iteration_statistics = '"{}"'.format(str(iteration)) + \
                           '"best_fitness": {}'.format(pop_statistics['best_fitness']) + \
                           '"worst_fitness": {}'.format(pop_statistics['worst_fitness']) + \
                           '"avg_fitness": {}'.format(pop_statistics['avg_fitness']) + \
                           '"std_dev_fitness": {}'.format(pop_statistics['std_dev_fitness']) + \
                           '"avg_mutation_step": {}'.format(pop_statistics['avg_mutation_step']) 

    print(iteration_statistics)
    logging.info(iteration_statistics)

    children = []
    for i in range(parent_couples_per_iteration):
      parents = select_parents(population)
      for j in range(children_amount_per_parent_pair):
        child = generate_offspring(parents)
        children.append(child)
        # print("GENERATED CHILD: {}".format(str(child)))
        
    population = kill_suckers(population, children, population_size)
  
  #plt.ioff(); plt.show()
  plot_array(avg_fitnesses, title = 'Fitness Average')
  plot_array(std_dev_fitnesses, title = 'Fitness Std Deviation')
  plot_array(avg_mutation_steps, title = 'Mutation Step Average')
  plot_array(std_dev_mutation_steps, title = 'Mutation Step Std Deviation')

  return

if __name__ == '__main__':
  main()
