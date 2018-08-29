import random
from restaurants import restaurants

samples = random.sample(set(restaurants), 3)
print(samples)

