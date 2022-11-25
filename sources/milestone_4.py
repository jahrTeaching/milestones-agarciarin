import matplotlib.pyplot as plt
import numpy as np

import common.cauchy_problem as cp
import common.convergence_rate as cr
import common.functions as fun
import common.problems.orbits as orb
import common.problems.oscillator as osc
import common.plots as plo
import common.richardson_error as re
import common.methods as met
import common.stability_regions as sr

def main():

    #Initialize values
    Dt = np.array([0.1, 0.01, 0.001])   #[s]
    tf = 14.                            #[s]
    #U0 = fun.init_state_vector_orbits(1, 1, 0) #(R[m], V[m/s], Zeta[deg]) -> Orbits
    U0 = np.array([1, 0])                     #(R[m], V[m/s], Zeta[deg]) -> Oscilator
    mets = [met.explicit_euler, met.runge_kutta4, met.inverse_euler, met.crank_nicolson, met.leap_frog]

    m = 2   #Nº points convergence
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
            q = fun.order(mets[i])
        
            """
            #Orbits
            U[i,:] = cp.cauchy_problem(U0, t, orb.orbits, mets[i])       #Cauchy solver orbits
            En[i,:] = orb.orbit_energy(U[i,:], t)                        #Energy orbit
            E[i,:] = re.richardson_error(U0, t, orb.orbits, mets[i], q)  #Error Richardson
            CR[i,:] = cr.convergence_rate(U0, t, orb.orbits, mets[i], m) #Convergence Rate
            """
        
            #Oscillator
            U[i,:] = cp.cauchy_problem(U0, t, osc.oscilator, mets[i])   
            #E[i,:] = re.richardson_error(U0, t, osc.oscilator, mets[i], q)  
            #CR[i,:] = cr.convergence_rate(U0, t, osc.oscilator, mets[i], m)


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


    
    #Stability
    a = 3
    n = 100
    x = np.linspace(-a, a, n)
    y = np.linspace(-a, a, n)
    ST = np.empty(len(mets), dtype=np.ndarray)

    for z in range(len(mets)):
        ST[z] = sr.stability_regions(x, y, mets[z])
        plo.plot_stability(x, y, ST[z], mets[z].__name__)

    

    #Graphics
    plo.plot_osc_dt(UU, TT, Dt, mets)

    #stab = sr.stability_regions(x, y, mets[4])
    #plo.plot_stability(x, y, stab)




    plt.draw()
    plt.pause(1)
    input("<Hit Enter To Close>")
    plt.close('all')


if __name__ == "__main__":
    main()

