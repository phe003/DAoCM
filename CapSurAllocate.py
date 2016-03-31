# -*- coding: utf-8 -*-
"""
Risk Surplus Model
Copyright by PwC

"""

import numpy as np
import sympy

def CapSurAllocate( A,M,Tar):
    A = np.mat(A)
    x = sympy.symbols('x') 
    x = sympy.solve([ A*M*np.transpose(A)*x**2-Tar**2],x)
    if len(x) == 1:
        return x[0][0]
    else:
        return x[1][0]