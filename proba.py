import numpy as np

import matplotlib.pyplot as plt

def proba(x, landa):

    norma = 1.0/(np.exp(-1) - np.exp(-20))
    return (norma/landa)*np.exp(-x/landa)

graf = np.linspace(1e-6, 100.0, 2000)

pos = [1.2, 2.5, 2.8, 5.0]

p = np.ones(len(graf))


for i in range(len(graf)):
    for j in range(len(pos)):

        p[i] = p[i] * proba(pos[j], graf[i])

p = p/(np.sum(p)*100.0/2000.0)
        
plt.plot(graf, p)
plt.xlabel("landa")
plt.ylabel("Probabilidad")
plt.title("Probabilidad vs landa")
plt.savefig("Probabilidad vs landa.png")







