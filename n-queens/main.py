import os
from algorithm import genetic_algorithm, stop_algorithm, choose_best_individual
from biology import generate_population
from queens import ChessBoard

def initialize(number_of_queens,
               population_size,
               number_of_sample_parents,
               recombination_probability,
               mutation_probability,
               max_fitness_evaluations):
  population = generate_population(population_size, number_of_queens)

  iteration_count = 0

  while not stop_algorithm(population, iteration_count, max_fitness_evaluations):
    population = genetic_algorithm(population,
                                   recombination_probability,
                                   mutation_probability,
                                   number_of_sample_parents)
    iteration_count += 1

  print('The algorithm ran for a total of {} iterations.'.format(iteration_count))

  best_individual = choose_best_individual(population)

  print('The fittest individual has fitness {}.'.format(best_individual.fitness))

  if (best_individual.fitness == 0):
    print('Queen positions:')
    for position in best_individual.queen_positions:
      print(ChessBoard.coordinate_to_chess_notation(position.row, position.column, number_of_queens))
  else:
    print('A valid solution was not found.')

if __name__ == '__main__':
  number_of_queens = os.getenv('NUMBER_OF_QUEENS', 8)
  population_size = os.getenv('POPULATION_SIZE', 100)
  number_of_sample_parents = os.getenv('NUMBER_OF_SAMPLE_PARENTS', 5)
  recombination_probability = os.getenv('RECOMBINATION_PROBABILITY', 0.9)
  mutation_probability = os.getenv('MUTATION_PROBABILITY', 0.4)
  max_fitness_evaluations = os.getenv('MAX_FITNESS_EVALUATIONS', 10000)

  initialize(number_of_queens,
             population_size,
             number_of_sample_parents,
             recombination_probability,
             mutation_probability,
             max_fitness_evaluations)
