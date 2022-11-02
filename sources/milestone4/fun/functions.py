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

def names_order(name_met):
    if name_met == 'Euler':
        method = met.explicit_euler
        q = 1
    elif name_met == 'RK4':
        method = met.runge_kutta4
        q = 4
    elif name_met == 'Inverse Euler':
        method = met.inverse_euler
        q = 1
    elif name_met == 'CN':
        method = met.crank_nicolson
        q = 2
    else:
        method = met.leap_frog
        q = 2

    return method, q
