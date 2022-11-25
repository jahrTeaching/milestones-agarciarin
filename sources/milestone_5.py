
import matplotlib.pyplot as plt
import numpy as np

from common.cauchy_problem import cauchy_problem
import common.functions as fn
import common.methods as met
import common.plot_n_body as plo_n
import common.problems.n_body as nb


Nb = 4 #Nº bodies
Nc = 3 #Nº coordinates

def main():

    #Initialize values
    Dt = 0.001   #[s]
    tf = 5
    N = int(tf/Dt)+1    #Nº steps
    t = np.linspace(0, tf, N)

    mets = [met.explicit_euler, met.runge_kutta4, met.inverse_euler, met.crank_nicolson, met.leap_frog]

    #U0 = fn.init_state_nbody_rand(Nb, Nc) #create random init values
    U0 = fn.init_state_nbody(Nb, Nc)
    U = np.zeros([len(U0), N])
    
    #Calculus
    i = 1 #Runge-Kutta
    U = cauchy_problem(U0, t, nb.n_body, mets[i]) 
    plo_n.plot_3D(U, t, Dt, mets[i], Nb, Nc)
    plo_n.plot_vel(U, t, Dt, mets[i], Nb, Nc)
    

if __name__ == "__main__":
    main()

    #manage pop ups
    plt.draw()
    plt.pause(1)
    input("<Hit Enter To Close>")
    plt.close('all')
