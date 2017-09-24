import random
import seaborn
import matplotlib.pylab as plt
import numpy as np
import pandas as pd

neighbor =  [[1, 3, 0, 0], [2, 4, 0, 1], [2, 5, 1, 2],
             [4, 6, 3, 0], [5, 7, 3, 1], [5, 8, 4, 2],
             [7, 6, 6, 3], [8, 7, 6, 4], [8, 8, 7, 5]]

neighbors = {i: neighbor[i] for i in range(9)}
def one_trial(t_max = 4):
    state_chains = []
    site = 8
    t = 0
    while t < t_max:
        t += 1
        site = neighbors[site][random.randint(0, 3)]
        state_chains.append(site)

    return state_chains

def test():
    steps = 100
    ensembles = []
    N_ens = 1000000
    for k in range(N_ens):
        ensembles.append(one_trial(steps)[-1])

    hist_nums, hist_idx = np.histogram(ensembles, bins=range(10))
    print(pd.DataFrame(np.array([hist_idx[:-1], hist_nums/N_ens]).T, columns=[u"site", u"probability"]))
    plt.figure()
    plt.plot(hist_idx[:-1],hist_nums/N_ens,"r*")
    plt.xlabel("State at {}th step".format(1))
    plt.ylabel("Frequencies / {} total trials " .format(N_ens))
    plt.show()
    # seaborn.distplot(ensembles, kde=False)
    # seaborn.plt.show()

    return ensembles

if __name__ == '__main__':
    ensembles = test()