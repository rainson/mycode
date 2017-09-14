# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 10:07:31 2017

@author: g00421879
"""

import numpy as np
import matplotlib.pylab as plt
import random
from math import exp
import seaborn

# H = -2J\sum_{<i,j>} s_i s_j

T = 50.0
J = 1.0
N = 100
Ksteps = 100000



class Ising_sample:
    def __init__(self, N, Ksteps):
        self.spin_state_init = np.ones(N)
        self.spin_state =  np.ones(N)
        self.sites = N
        self.steps = Ksteps
        self.select_probability = 1.0/N
#        self.samples = []
        

    def get_delta_energy(self,site_idx):
        spin_old = self.spin_state[site_idx] 
        spin_new = -spin_old
        if site_idx < self.spin_state.size-1:
            dE = -2*J*((spin_new - spin_old) * self.spin_state[site_idx -1]+ 
                   (spin_new - spin_old) * self.spin_state[site_idx +1])
        elif site_idx == self.spin_state.size-1:
            dE = -2*J*((spin_new - spin_old) * self.spin_state[site_idx -1]+ 
                   (spin_new - spin_old) * self.spin_state[0])
        return dE


    def accept_ration(self, delta_energy):
        
        apt_rat = None
        if delta_energy > 0:
            apt_rat = exp(-delta_energy/T)
        else:
            apt_rat = 1.0
        return apt_rat
    

    def spin_one_flip(self,  site_idx):
        rand_select = random.random()
        randb_accept = random.random()
        spin_state_old = self.spin_state
        
        if rand_select < self.select_probability:
            delta_energy = self.get_delta_energy(site_idx)
            act_prob = self.accept_ration(delta_energy)
#            print act_prob
            if randb_accept < act_prob:
                self.spin_state[site_idx] = - spin_state_old[site_idx]
#                print site_idx , self.spin_state[site_idx]
    
    def spin_all_flips(self):
        for site_idx in range(self.sites):
            self.spin_one_flip(site_idx)
            
    def get_all_samples(self):
        samples = []
        for k in range(self.steps):
#            if k>1:
            if k%(Ksteps//10)==0:
                print "epoch is: {} ".format(k)
            self.spin_all_flips()
#            print self.spin_state
            samples.append(self.spin_state.copy())
        return samples
            
        
def get_energy(spin_state):
    bind_energy = -2*J
    energy = 0.
    for site_idx in range(spin_state.size):
        energy = energy + bind_energy*spin_state[site_idx-1]*spin_state[site_idx]
    return energy
    



if __name__ == "__main__" :
    Isamp = Ising_sample(N, Ksteps)
#    random.seed(2000)
    samples = Isamp.get_all_samples()
    energies = []
    for spin_state in samples:
        energy = get_energy(spin_state)
        energies.append(energy)
    seaborn.distplot(energies)
    
#    Isamp.get_all_samples()
    



    

        
