#functions initiate state vector and plots
import math

import numpy as np
import common.methods as met

#Initiate Vector
def init_state_vector_orbits(r, v, zeta):
    zetaRad = math.radians(zeta)
    rx = r*math.cos(zetaRad)
    ry = r*math.sin(zetaRad)
    vx = -v*math.sin(zetaRad)
    vy = v*math.cos(zetaRad)
    return np.array([rx, ry, vx, vy])

#Methods order
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


#Initiate n_body problem conditions with random values
def init_state_nbody_rand(Nb, Nc):
    rg = [0, 2]
    U0 = np.random.uniform(rg[0], rg[1], 2*Nb*Nc)
    U1 = np.reshape(U0, (Nb, Nc, 2)) #N_bodies, N_coord, pos&vel

    return U0

#Initiate n_body problem conditions manually
def init_state_nbody(Nb, Nc):
    U0 =  np.zeros(2*Nc*Nb)
    U1  = np.reshape(U0, (Nb, Nc, 2))
    
    # body 1 
    r1 = [1, 0, 0]
    v1 = [0, 0.5, 0]

    # body 2 
    r2= [-1, 0, 0]
    v2 = [0, -0.5, 0] 
    
    # body 3 
    r3 = [0, 1, 0] 
    v3 = [-0.5, 0, 0] 
         
    # body 4 
    r4 = [0, -1, 0] 
    v4 = [0.5, 0, 0]  
    """
    # body 1 
    r1 = [1, 0, 0]
    v1 = [0, 0.5, 0]

    # body 2 
    r2= [-1, 1.4, 0]
    v2 = [-0.35, -0.35, 0] 
    
    # body 3 
    r3 = [-1, -1.4, 0] 
    v3 = [0.35, -0.35, 0] 
         
    # body 4 
    r4 = [0, -1, 0] 
    v4 = [0.5, 0, 0] 
    """

    r = np.concatenate(([r1], [r2], [r3], [r4]), axis=0)
    v = np.concatenate(([v1], [v2], [v3], [v4]), axis=0)

    for i in range(Nb):
        U1[i, :, 0] = r[i,:]
        U1[i, :, 1] = v[i,:]

    return U0
