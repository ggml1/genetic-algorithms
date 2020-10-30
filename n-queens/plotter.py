import matplotlib.pyplot as plt
import numpy as np

populations = ['10','30','50','70','100','120','150','200','250','300','400','500']

std_deviation_population = [3348.57,
                            396.07,
                            232.64,
                            807.11,
                            235.36,
                            91.51,
                            87.61,
                            66.67,
                            101.91,
                            90.21,
                            79.53,
                            80.03]

avg_iterations_population = [ 1655.5,
                              291.56,
                              141.4,
                              425.23,
                              139.43,
                              103.33,
                              76.6,
                              81.93,
                              110.8,
                              96.4,
                              113.93,
                              111.93]

x = populations

y = avg_iterations_population
fig, ax = plt.subplots()
ax.bar(x, y)
ax.set_title('Population Size x Average Iterations (30 runs)')
plt.xticks(x)
plt.savefig('population_iterations_average.png')


y = std_deviation_population
fig, ax = plt.subplots()
ax.bar(x, y)
ax.set_title('Population Size x Standard Deviation of Iterations (30 runs)')
plt.xticks(x)
plt.savefig('population_iterations_std_deviation.png')

avg_fitness_population = [-0.97,
                          -1.29,
                          -1.77,
                          -1.92,
                          -2.38,
                          -2.57,
                          -3.18,
                          -3.27,
                          -3.17,
                          -3.46,
                          -3.44,
                          -3.66]
std_deviation_fitness_population = [0.21,
                                    0.60,
                                    1.00,
                                    0.95,
                                    1.06,
                                    0.97,
                                    0.95,
                                    0.88,
                                    0.90,
                                    0.79,
                                    0.62,
                                    0.54]

y = avg_fitness_population
fig, ax = plt.subplots()
ax.bar(x, y)
ax.set_title('Population Size x Average Fitness (30 runs)')
plt.xticks(x)
plt.savefig('population_fitness_average.png')


y = std_deviation_fitness_population
fig, ax = plt.subplots()
ax.bar(x, y)
ax.set_title('Population Size x Standard Deviation of Fitness (30 runs)')
plt.xticks(x)
plt.savefig('population_fitness_standard_deviation.png')


selection_method = ['Best 2 out of 5', 'Roulette of 5']
avg_iterations = [234.5, 522.36]
std_dev_iterations = [501.2, 650.44]
avg_fitness = [-2.24, -1.691]
std_dev_fitness = [1.06, 0.93]

x = selection_method

y = avg_iterations
fig, ax = plt.subplots()
ax.bar(x, y)
ax.set_title('Selection Algorithm x Average Iterations(30 runs)')
plt.xticks(x)
plt.savefig('selection_average_iterations.png')

y = std_dev_iterations
fig, ax = plt.subplots()
ax.bar(x, y)
ax.set_title('Selection Algorithm x Standard Deviation of Iterations (30 runs)')
plt.xticks(x)
plt.savefig('selection_iterations_std_deviation.png')

y = avg_fitness
fig, ax = plt.subplots()
ax.bar(x, y)
ax.set_title('Selection Algorithm x Average Fitness (30 runs)')
plt.xticks(x)
plt.savefig('selection_fitness_average.png')

y = std_dev_fitness
fig, ax = plt.subplots()
ax.bar(x, y)
ax.set_title('Selection Algorithm x Standard Deviation of Fitness (30 runs)')
plt.xticks(x)
plt.savefig('selection_fitness_std_deviation.png')


average_100_convergence = ['Best 2 out of 5', 'Roulette of 5']
x = average_100_convergence
roulette_100_conv_avg = [469.26, 578.83]
roulette_100_conv_deviation = [324.74, 505.68]

y = roulette_100_conv_avg
fig, ax = plt.subplots()
ax.bar(x, y)
ax.set_title("Selection Algorithm x Average Iterations (30 runs, 100% convergence)")
plt.xticks(x)
plt.savefig('selection_average_iterations_100_percent.png')

y = roulette_100_conv_deviation
fig, ax = plt.subplots()
ax.bar(x, y)
ax.set_title("Selection Algorithm x Std Dev of Iterations (30 runs, 100% convergence)")
plt.xticks(x)
plt.savefig('selection_deviation_iterations_100_percent.png')






populations = ['10','30','50','70','100','120','150','200','250','300','400','500']

std_deviation_population_100 = [269.55,
490.98,
330.11,
451.25,
114.50,
110.70,
190.66,
273.76,
223.94,
251.01,
217.85,
243.76]

avg_iterations_population_100 = [330.3,
  435.5,
  341.7,
  463.6,
  387.8,
  428.8,
  612.3,
  841.5,
  925.5,
  1259.5,
  1584.03,
  2030.2 ]



x = populations
y = avg_iterations_population_100
fig, ax = plt.subplots()
ax.bar(x, y)
ax.set_title("Population Size x Avg Iter. (30 runs, 100% Convergence)")
plt.xticks(x)
plt.savefig("population_iterations_average_100_percent.png")


y = std_deviation_population_100
fig, ax = plt.subplots()
ax.bar(x, y)
ax.set_title("Population Size x Std Dev of Iterations (30 runs, 100% Convergence)")
plt.xticks(x)
plt.savefig("population_iterations_std_deviation_100_percent.png")