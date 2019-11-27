
import numpy as np
import matplotlib.pyplot as plt

population = 2000

AA = int(population*0.3)
aa = int(population*0.4)
Aa = population-AA-aa

past_data = []

ROUNDS = 500
for i in range(ROUNDS):
    #  if i == 250: ## immigrate
    #      AA += population
    #      AA = int(AA/2)
    #      aa = int(aa/2)
    #      Aa = population - AA - aa 

    AA -= np.random.binomial(AA, 0.9)
    Aa -= np.random.binomial(Aa, 0.0)
    aa -= np.random.binomial(aa, 0.9)

    cur_population = AA + Aa + aa
    moms = np.random.choice(["AA", "Aa", "aa"], size = population, p=[AA/cur_population, Aa/cur_population, aa/cur_population])
    dads = np.random.choice(["AA", "Aa", "aa"], size = population, p=[AA/cur_population, Aa/cur_population, aa/cur_population])
    mom_alleles = [np.random.choice(list(mom)) for mom in moms]
    dad_alleles = [np.random.choice(list(dad)) for dad in dads]
    kids = np.array([mom_alleles[i]+dad_alleles[i] for i in range(population)])
    AA = np.sum(kids=="AA")
    aa = np.sum(kids=="aa")
    Aa = population - AA - aa

    past_data.append([AA,Aa,aa])

AAs = [x[0] for x in past_data]
Aas = [x[1] for x in past_data]
aas = [x[2] for x in past_data]

print(np.average(AAs[ROUNDS//2:])/population, np.average(Aas[ROUNDS//2:])/population, np.average(aas[ROUNDS//2:])/population)

plt.plot(AAs, c='r', label="AA")
plt.plot(Aas, c='b', label="Aa")
plt.plot(aas, c='k', label="aa")
plt.legend()
plt.show()


