from scipy.optimize import newton
import numpy as np


def explicit_euler(U, dt, t, f):
    return U + dt*f(U, t)

def runge_kutta4(U, dt, t, f):
    k1 = f(U, t)
    k2 = f(U+dt*k1/2, t)
    k3 = f(U+dt*k2/2, t)
    k4 = f(U+dt*k3, t)
    return U + dt*(k1 + 2*k2 + 2*k3 + k4)/6

def inverse_euler(U, dt, t, F): 
    def residual(X): 
        return X - U - dt * F(X, t)
    return newton(func = residual, x0 = U, tol = 10e-5, maxiter = 10000) #tol: error of the zero value (necesarry if not RuntimeError)

def crank_nicolson(U, dt, t, F): 
    def residual_cn(X):        
         return  X - a - dt/2 *  F(X, t + dt)
    a = U  +  dt/2 * F(U, t)  
    return newton(residual_cn, U)

def leap_frog(U_prev, U, dt, t, f):
    return U_prev + 2*dt*f(U, t)
