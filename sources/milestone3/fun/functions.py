#functions initiate state vector and plots
import math

import numpy as np


#Initiate Vector
def init_state_vector(r, v, zeta):
    zetaRad = math.radians(zeta)
    rx = r*math.cos(zetaRad)
    ry = r*math.sin(zetaRad)
    vx = -v*math.sin(zetaRad)
    vy = v*math.cos(zetaRad)
    return np.array([rx, ry, vx, vy])
