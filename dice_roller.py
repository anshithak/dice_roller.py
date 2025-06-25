import numpy as np
def uniform(n, m):
  return np.random.randint(1, n+1, size = m)
print(uniform(6, 1))