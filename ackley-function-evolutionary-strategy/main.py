from biology import *
from utils import population_average_fitness, population_best_fitness, population_worst_fitness
import matplotlib.pyplot as plt

def main(number_of_iterations = 10000, population_size = 50, offspring_size = 100):
  population = generate_population(population_size)
  
  for iteration in range(number_of_iterations):
    #sca = plt.scatter(iteration, population_average_fitness(population), s=200, lw=0, c='red', alpha=0.5); plt.pause(0.05)

    #print("Iteration: {} - AVG Fitness: {} - Best Fitness: {} - Worst Fitness {}".format(str(iteration), population_average_fitness(population), population_best_fitness(population), population_worst_fitness(population)))
    print("Iteration: {} - Best Fitness: {} - Worst Fitness {}".format(str(iteration), population_best_fitness(population), population_worst_fitness(population)))

    children = []
    for i in range(offspring_size):
      parents = local_parents_selection(population)
      child = generate_offspring(parents)
      children.append(child)
      # print("GENERATED CHILD: {}".format(str(child)))
        
    population = kill_suckers(children, population_size)
  
  #plt.ioff(); plt.show()

  return

if __name__ == '__main__':
  main()
