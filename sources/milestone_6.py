import matplotlib.pyplot as plt
import numpy as np

import common.methods.methods as met
import common.problems.rest_3b as r3b
import common.plots.plot_lagr as plag
from common.methods.embedded_rk import embedded_rk
from common.functions import init_lagr_points
from common.cauchy_problem import cauchy_problem
from random import uniform


def main():

    ##Initialize values
    Dt = 0.001      #[s]
    tf = 10        #[s]
    N = int(tf/Dt)+1    #Nº steps
    t = np.linspace(0, tf, N)

    Nl = 5 #Nº lagrange points
    Nc = 3 #Nº coord
    Lp_U0 = init_lagr_points(Nl, Nc)

    ##Choose Numerical Method
    mets = [met.explicit_euler, met.runge_kutta4, met.inverse_euler, met.crank_nicolson, met.leap_frog, embedded_rk]
    i = 5 #RK Embedded (5)


    ##Lagrange Points
    Lp = r3b.lagr_points(Lp_U0, Nl, Nc)
    plag.plot_lagr(Lp)
    print("Lp=", Lp)

    
    ##Orbits around Lagrange Points
    U0 = np.empty([Nl, 2*Nc])
    UU = np.empty([Nl], dtype=type(U0))

        #Initialize orbits around Langrage Points 
    rand = uniform(0, 1e-5) 
    U0[:,0:Nc] = Lp + rand  #Position Lagr Points
    U0[:,Nc:2*Nc] = 0       #Vel Lagr Points

    for j in range(Nl):
        U = cauchy_problem(U0[j,:], t, r3b.rest_3b, mets[i])  
        UU[j] = U 

        plag.plot_one_orb_lagr(Lp[j], U, j+1, mets[i])

        #Plots all orbits around Lagrange Points
    plag.plot_orb_lagr(Lp, UU, mets[i])
    

    ##Stability Langrage Points
    Lp0 = np.empty([Nl, 2*Nc])
    Lp0[:,0:Nc] = Lp    #Position Lagr Points
    Lp0[:,Nc:2*Nc] = 0  #Vel Lagr Points

    for k in range(len(Lp0)):
        val, vect = r3b.lagr_points_stab(Lp0[k])
        plag.plot_stab(val, k+1)


if __name__ == "__main__":
    main()

    #manage pop ups
    plt.draw()
    plt.pause(1)
    input("<Hit Enter To Close>")
    plt.close('all')
