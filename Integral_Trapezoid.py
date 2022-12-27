import numpy as np
import matplotlib.pyplot as pd

def trapezoid(f,a,b,n):
    h=(b-a)/n
    sum=0.0
    for i in range(1,n):
        x=a+i*h
        sum=sum+f(x)
    integral=(h/2)*(f(a)+2*sum+f(b))
    return integral

def f(x):
    return x**2+21

a=8.0
b=10.0
n=120

integral=trapezoid(f,a,b,n)

print('Integral = ', integral)
