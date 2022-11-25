import numpy as np
from milestone_5 import Nb, Nc


def n_body(U, t):
    Us  = np.reshape(U, (Nb, Nc, 2))  
    F =  np.zeros(len(U))   
    dUs = np.reshape(F, (Nb, Nc, 2))  
    
    r = np.reshape(Us[:, :, 0], (Nb, Nc))   #pos
    v = np.reshape(Us[:, :, 1], (Nb, Nc))   #vel
    
    drdt = np.reshape(dUs[:, :, 0], (Nb, Nc))   #vel
    dvdt = np.reshape(dUs[:, :, 1], (Nb, Nc))   #accel

    dvdt[:,:] = 0  #WARNING
    
    for i in range(Nb):   
        drdt[i,:] = v[i,:]
        for j in range(Nb): 
            if j != i:  
                d = r[j,:] - r[i,:]
                dvdt[i,:] = dvdt[i,:] +  d[:] / np.linalg.norm(d)**3 

    return F
    