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
    U0 = np.random.uniform(0, 1, 2*Nb*Nc)
    U1 = np.reshape(U0, (Nb, Nc, 2)) #N_bodies, N_coord, pos&vel

    return U0

#Initiate n_body problem conditions manually
def init_state_nbody(Nb, Nc):
    U0 =  np.zeros(2*Nc*Nb)
    U1  = np.reshape(U0, (Nb, Nc, 2))  
    r0 = np.reshape(U1[:, :, 0], (Nb, Nc)) 
    v0 = np.reshape(U1[:, :, 1], (Nb, Nc))

    # body 1 
    r0[0,:] = [1, 0, 0]
    v0[0,:] = [0, 0.4, 0]

    # body 2 
    r0[1,:] = [-1, 0, 0]
    v0[1,:] = [0, -0.4, 0] 
    
    # body 3 
    r0[2, :] = [0, 1, 0] 
    v0[2, :] = [-0.4, 0, 0] 
         
    # body 4 
    r0[3, :] = [0, -1, 0] 
    v0[3, :] = [0.4, 0, 0]  
    
    return U0
    