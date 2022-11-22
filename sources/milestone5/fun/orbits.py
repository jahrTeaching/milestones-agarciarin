from numpy import array, zeros

import fun.constant as cte

#Kepler orbit
def orbits(U, t):
    d = (U[0]**2 + U[1]**2)**1.5
    rx = -U[0]/d
    ry = -U[1]/d
    dxdt = U[2]
    dydt = U[3]
    return array([dxdt, dydt, rx, ry])

#Orbit energy
def orbit_energy(U, t):
    e = array(zeros(len(t)))

    for i in range(len(t)):
        Ek = (U[2,i]**2 + U[3,i]**2)/2  #Kinetic energy
        Ep = -cte.EARTHMU/(U[0,i]**2 + U[1,i]**2)**0.5 #Potential energy
        e[i] = Ek + Ep
    
    return e
