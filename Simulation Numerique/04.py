def factorille(n):
    fact =1
    for i in range(1,n+1) :
        fact *= i
    return fact

# 2
import math
import numpy as np
def stirling(n) :
    # return (2*math.pi*n(n/math.e)**2n)**(1/2)
    # return math.sqrt(2*math.pi*n(n/math.e)**n)
    return np.sqrt(2*np.pi*n)*(n/np.exp(1) ) **n

