#functions initiate state vector and plots
import math

import numpy as np
import fun.methods as met

#Initiate Vector
def init_state_vector_orbits(r, v, zeta):
    zetaRad = math.radians(zeta)
    rx = r*math.cos(zetaRad)
    ry = r*math.sin(zetaRad)
    vx = -v*math.sin(zetaRad)
    vy = v*math.cos(zetaRad)
    return np.array([rx, ry, vx, vy])

def order(mets):
    if mets == met.explicit_euler:
        q = 1
    elif mets == met.runge_kutta4:
        q = 4
    elif mets == met.inverse_euler:
        q = 1
    elif mets == met.crank_nicolson:
        q = 2
    else:
        q = 2

    return q
