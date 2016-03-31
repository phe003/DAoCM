# -*- coding: utf-8 -*-
"""
Risk Surplus Model
Copyright by PwC

"""

import math;
import numpy as np;

def mc (A, M):
    A = np.mat(A);
    res = math.sqrt(A * M * A.T)
    return res 