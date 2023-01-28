from math import cos
from math import sin
from math import acos
from math import pi
from math import sqrt
import os
import scipy.integrate as integrate
os.system('cls')

a = sqrt(14)
#define funtion x and y according to t
def fun_x(x):
    return sqrt(14)*cos(x)

def fun_y(x):
    return sqrt(14)*sin(x)
#define a function to calculate differential equation
def d_fun(x, val):
    h = 1e-5
    if val=='x':
        return (fun_x(x+h)-fun_x(x-h))/(2*h)
    elif val=='y':
        return (fun_y(x+h)-fun_y(x-h))/(2*h)
#calculate the work
result = integrate.quad(lambda t: 2*(a*sin(t))**1.5*d_fun(t,'x') + 3*a*cos(t)*(a*sin(t))**0.5*d_fun(t,'y'), acos(1/a), pi/2)
print(result)

# print("The work done is %.4f"%result + " (J)")