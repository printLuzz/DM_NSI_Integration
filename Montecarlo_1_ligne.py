import random
print(sum([1 for _ in range(1_000_000) if random.random()**2 >= random.random()])/1_000_000)
           
# by Anselem Peña