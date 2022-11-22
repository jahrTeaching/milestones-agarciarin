import time
import matplotlib.pyplot as plt
import numpy as np

import fun.cauchy_problem as cp
import fun.functions as fn
import fun.methods as met
import fun.n_body as nb
import fun.plots as plo
import fun.plot_n_body as plo_n



def main():

    #Initialize values
    Dt = 0.1   #[s]
    tf = 1
    N = int(tf/Dt)+1            #Nº steps
    t = np.linspace(0, tf, N)

    mets = [met.explicit_euler, met.runge_kutta4, met.inverse_euler, met.crank_nicolson, met.leap_frog]

    Nb = 4 #Nº bodies
    Nc = 3 #Nº coordinates
    #U0 = fn.init_state_nbody_rand(Nb, Nc)
    U0 = fn.init_state_nbody(Nb, Nc)
    U = np.zeros([len(mets), len(U0), N])


    #Calculus
    #for i in range(len(mets)):
    #    U[i,:] = cp.cauchy_problem(U0, t, nb.n_body, mets[i]) 




    #tests
    Dt__ = 0.01
    tf__ = 10
    t__ = np.linspace(0, tf__, int(tf__/Dt__)+1)
    U__ = cp.cauchy_problem(U0, t__, nb.n_body, mets[1])
    plo_n.plot_3D(U__, t__, Dt__, mets[1], Nb, Nc)


    plt.draw()
    plt.pause(1)
    input("<Hit Enter To Close>")
    plt.close('all')


if __name__ == "__main__":
    main()
