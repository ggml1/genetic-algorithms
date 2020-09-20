# n-Queens

The n-Queen problem is the challenge of finding a placement of queens on the chessboard where no two queens can attack each other.

It is possible to find all solutions using backtrack techniques. We can leverage genetic algorithms to search for a valid solution for it.

## Algorithm

The model has the following attributes:

- Population size of 100
- Each individual's chromosome is, initially, a randomly generated placement of queens on a chessboard
- The algorithm perform at most 10000 fitness evaluations
- At each evaluation, five individuals are chosen randomly. The best two of this chosen set become parents of that iteration
- They will reproduce with a 90% probability of recombination
- Cut-and-crossfill crossover technique is used during recombination
- Mutations occur with a 40% probability
- Two children are generated at each reproduction step
- Survivors are chosen by eliminating individuals with lowest fitness

Some attributes can be changed using environment variables:

- `NUMBER_OF_QUEENS` the `n` of our problem. Defaults to `8`.
- `NUMBER_OF_SAMPLE_PARENTS` the number of individuals randomly chosen. From those, the two with highest fitness will be the parents of their iteration. Defaults to `5`.
- `POPULATION_SIZE` the population size used. Defaults to `100`.
- `RECOMBINATION_PROBABILITY` how often recombinations occur in the reproduction step. Defaults to `0.9 (90%)`.
- `MUTATION_PROBABILITY` how often mutations occur during reproduction. Defaults to `0.4 (40%)`
- `MAX_FITNESS_EVALUATIONS` maximum number of iterations the generic algorithm will be run for. Defaults to `10000`. 

### Fitness

Here, we want a function that approaches its maximum depending on how close we are to a solution.

We can use the number of collisions between queens as a metric. When closer to a solution, the number of collisions will become gradually smaller.

We can have our functions' maximum equal to 0, which means no collisions. A function that would have this behavior would be:

```
f(S) = -1 * C(S)
```

Where `C(S)` is the total number of collisions considering all pairs of queens on the chessboard `S`.

## Running

You can use `pipenv` to run the project as follows:

- Run `pipenv install` to download dependencies
- Run `pipenv run python3 main.py` to run the project
