from math import *

import scipy.integrate as integrate


a = 2

def x(t):
    return sqrt(a)*cos(t)

def y(t):
    return sqrt(a)*sin(t)


a_value = acos(1/sqrt(a))   
b_value = pi/2     

F_func = lambda t: 2*y(t)**1.5*(-y(t)) + 3*x(t)*y(t)**0.5*x(t)

result = integrate.quad(F_func, a_value, b_value)
W_Force= round(result[0],3)

print("The work force is  " + str(W_Force) + "(J)")