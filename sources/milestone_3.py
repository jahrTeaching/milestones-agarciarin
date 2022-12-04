import matplotlib.pyplot as plt
import numpy as np

import common.cauchy_problem as cp
import common.convergence_rate as cr
import common.functions as fun
import common.methods.methods as met
import common.problems.orbits as orb
import common.plots.plots as plo
import common.richardson_error as re


def main():

    #Initiate values
    print("Introduzca dt = ")
    dt = float(input())
    #dt = 0.1       #[s] 
    tf = 30.        #[s]

    R0 = 1.         #[m]
    V0 = 1.         #[m/s]
    Zeta0 = 0.      #[deg]

    N = int(tf/dt)+1    #Nº steps
    t = np.linspace(0, tf, N)
    U0 = fun.init_state_vector_orbits(R0, V0, Zeta0)
    mets = [met.explicit_euler, met.runge_kutta4, met.inverse_euler, met.crank_nicolson, met.leap_frog]

    m = 5   #Nº points convergence
    U = np.zeros([len(mets), len(U0), N])
    En = np.zeros([len(mets), N])
    E = np.zeros([len(mets), len(U0)+1, N])
    CR = np.zeros([len(mets), 2, m])

    #Calculus
    for i in range(len(mets)):
        if mets[i] == 'Euler':
            method = met.explicit_euler
            q = 1
        elif mets[i] == 'RK4':
            method = met.runge_kutta4
            q = 4
        elif mets[i] == 'Inverse Euler':
            method = met.inverse_euler
            q = 1
        else:
            method = met.crank_nicolson
            q = 2
    
        U[i,:] = cp.cauchy_problem(U0, t, orb.orbits, method)       #Cauchy solver orbits
        En[i,:] = orb.orbit_energy(U[i,:], t)                       #Energy orbit
        E[i,:] = re.richardson_error(U0, t, orb.orbits, method, q)  #Error Richardson
        CR[i,:] = cr.convergence_rate(U0, t, orb.orbits, method, m) #Convergence Rate
    
    #Graphics
    plo.plot_positions(U, mets, dt)
    plo.plot_energy(En, mets, t, dt)
    plo.plot_error(E, mets, t, dt)
    plo.plot_met_error(E, mets, t, dt)
    plo.plot_conv_rate(CR, mets, dt)
    plo.plot_comparision_cr(CR, mets, dt)

    plt.draw()
    plt.pause(1)
    input("<Hit Enter To Close>")
    plt.close('all')
    

if __name__ == "__main__":
    main()
