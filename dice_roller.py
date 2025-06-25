import numpy as np
def uniform(n, m):
  return np.random.randint(1, n+1, size = m)
print("The random value on the die after rolling is",uniform(6, 1))