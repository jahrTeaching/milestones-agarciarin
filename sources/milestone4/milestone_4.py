import matplotlib.pyplot as plt
import numpy as np
from pandas import array

import fun.cauchy_problem as cp
import fun.convergence_rate as cr
import fun.functions as fun
import fun.orbits as orb
import fun.oscillator as osc
import fun.plots as plo
import fun.richardson_error as re

def main():

    #Initialize values
    Dt = np.array([0.1, 0.01, 0.001])   #[s]
    tf = 14.                            #[s]
    #U0 = fun.init_state_vector_orbits(1, 1, 0) #(R[m], V[m/s], Zeta[deg]) -> Orbits
    U0 = np.array([1, 0])                     #(R[m], V[m/s], Zeta[deg]) -> Oscilator
    mets = np.array(["Euler", "RK4", "Inverse Euler", "CN", "Leap Frog"])

    m = 5   #Nº points convergence
    UU = np.empty(len(Dt), dtype=np.ndarray)
    TT = np.empty(len(Dt), dtype=np.ndarray)

    #Calculus
    for j in range(len(Dt)):
        N = int(tf/Dt[j])+1            #Nº steps
        t = np.linspace(0, tf, N)

        U = np.zeros([len(mets), len(U0), N])
        En = np.zeros([len(mets), N])
        E = np.zeros([len(mets), len(U0)+1, N])
        CR = np.zeros([len(mets), 2, m])

        for i in range(len(mets)):
            method, q = fun.names_order(mets[i])
        
            """
            #Orbits
            #U[i,:] = cp.cauchy_problem(U0, t, orb.orbits, method)       #Cauchy solver orbits
            #En[i,:] = orb.orbit_energy(U[i,:], t)                       #Energy orbit
            #E[i,:] = re.richardson_error(U0, t, orb.orbits, method, q)  #Error Richardson
            #CR[i,:] = cr.convergence_rate(U0, t, orb.orbits, method, m) #Convergence Rate
            """
        
            #Oscillator
            U[i,:] = cp.cauchy_problem(U0, t, osc.oscilator, method)   
            #E[i,:] = re.richardson_error(U0, t, osc.oscilator, method, q)  
            #CR[i,:] = cr.convergence_rate(U0, t, osc.oscilator, method, m)

        UU[j] = U
        TT[j] = t

        #Graphics
        #plo.plot_positions(U, mets, Dt[j])
        #plo.plot_energy(En, mets, t, Dt[j])
        #plo.plot_error(E, mets, t, Dt[j])
        #plo.plot_met_error(E, mets, t, Dt[j])
        #plo.plot_conv_rate(CR, mets, Dt[j])
        #plo.plot_comparision_cr(CR, mets, Dt[j]) 


        #plo.plot_oscillator(U[4,:], t, Dt[j], "LeapFrog")
        #plo.subplot_oscillators(U, t, mets, Dt[j])


    #Graphics
    plo.plot_osc_dt(UU, TT, Dt, mets)


    plt.draw()
    plt.pause(1)
    input("<Hit Enter To Close>")
    plt.close('all')


if __name__ == "__main__":
    main()

