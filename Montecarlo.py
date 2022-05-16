import random

def f(x):
    return x**2

somme = 0
for _ in range(1_000_000):
    x = random.random()    
    y = random.random()
    if f(x) >= y:
        somme += 1
print(somme / 1_000_000)