# -*- coding: utf-8 -*-

import numpy as np

class peddls2D:
    
    def __init__(self, peddle_size_x, peddle_size_y):
        self.peddle_size = peddle_size_x*peddle_size_y
        self.peddle_size_x = peddle_size_x
        self.peddle_size_y = peddle_size_y
        self.site_prob = [0.0]*self.peddle_size
        self.neighbors = [[0]*4 ]*self.peddle_size
        
    def get_neighbors(self):
        for site in range(self.peddle_size):
            
