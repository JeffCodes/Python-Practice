# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 15:57:24 2015

@author: BergemJE
"""

import numpy as np
import pandas as pd

x = np.matrix( ((2,3), (3, 5)) )
y = np.matrix( ((1,2), (5, -1)) )

x * y

j = np.matrix( ((6,6,2,8), (8, 8,4,6), (10,10,3,4), (4, 8,10,8), (1, 4,3,10)) )
p = np.matrix( ((10,4,1,2), (-1, -2,-10,-6), (4,10,2,8), (2, 8,2,10)) )

u = j * p

df = pd.DataFrame(u, index=['BSF','HF','IB','St', 'GS'], columns=['MG','En','Sl','Ac'])