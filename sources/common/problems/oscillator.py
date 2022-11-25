from numpy import array

def oscilator(U, t):
    return array( [U[1], -U[0]] )
