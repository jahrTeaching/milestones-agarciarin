import numpy as np
import constant

#Kepler orbit
def Orbits(U, t):
    d = (U[0]**2 + U[1]**2)**1.5
    rx = -U[0]/d
    ry = -U[1]/d
    dxdt = U[2]
    dydt = U[3]
    return np.array([dxdt, dydt, rx, ry])

#Orbit energy
def OrbitEnergy(U, t):
    e = np.array(np.zeros(len(t)))

    for i in range(len(t)):
        Ek = (U[2,i]**2 + U[3,i]**2)/2  #Kinetic energy
        Ep = -constant.MU_earth/(U[0,i]**2 + U[1,i]**2)**0.5 #Potential energy
        e[i] = Ek + Ep
    
    return e