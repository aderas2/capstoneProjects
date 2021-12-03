#Law of Large Numbers
import numpy as np
from numpy.random import randn
N = 1000000
counter = 0
for i in randn(N):
  if i > -1 and i<1:
    counter = counter + 1
print(counter/N)