#main
import numpy as np
import functions as fun
import matplotlib.pyplot as plt

#const
R0 = 1.     #[m]
V0 = 1.     #[m/s]
Zeta0 = 0.  #[deg]
t0 = 0.     #[s]
dt = 10**-2 #[s] 
tf = 10.    #[s]
N = int(tf/dt)+1

X_Euler = np.zeros([5,N]) #State vector [rx, ry, vx, vy, t]
X0_Euler = fun.InitStateVector(R0, V0, Zeta0, t0)
X_Euler[:,0] = X0_Euler

#Explicit Euler
X_Euler = fun.ExplicitEuler(X_Euler, dt, N)

#Graphics
fun.plot_Position(X_Euler)
fun.plot_V_vs_T(X_Euler, N)
plt.show()