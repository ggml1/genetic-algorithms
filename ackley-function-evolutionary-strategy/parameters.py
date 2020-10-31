params = {
  # n parameter of the ackley function. Also used for inidividual chromosome definition. [1 - inf]
  "ACK_N": 30,
  # Max amout of allowed iterations [1 - inf]
  "ITR_AMT": 10000,
  # Higher and lower bounds for chromosome initialization. [-inf - +inf]
  "LWR_BND": -15,
  "UPR_BND": 15,
  # Population Size [1 - inf]
  "POP_SIZE": 50,
  # Parent couples selected from the population per iteration [1 - POP_SIZE/2]
  "PRT_CPL": 400,
  # Amount of children generated by a single pair of parents, per iteration [1 - inf]
  "CHL_PPR": 1,
  # Mutation Step Size [0.0 - 1.0]
  "MUT_STP": 0.5,
  # Learning rate multiplier [0.0 - 1.0]
  "LRN_RT_MLT": 1.0,
  # Floor of mutation step [0.0 - 1.0]
  "EPS_ZRO": 0.00001,
  # Mutation Probability [0.0 - 1.0]
  "MUT_PRB": 0.85,
  # Mutation Type [UNCORRELATED_SINGLE, UNCORRELATED_MANY]
  "MUT_TYP": "UNCORRELATED_SINGLE",
  # Survival Strategy [REPLACE_PARENTS, BEST_FIT, BALANCED]
  "SRV_STR": "REPLACE_PARENTS",
  # Recombination Type [INTERMEDIATE, DISCRETE]
  "RECOMB_TYPE": "INTERMEDIATE",
  # Parent selection strategy [LOCAL, GLOBAL]
  "PRNT_SEL": "LOCAL"
}
