def EstPremier(n):
    """
        Teste si n est un nombre premier en verifiant
    """
    i=2
    while i**2 <= n:
        if n % i == 0 :
            return False
        i += 1
    return True
def pi(n):
    s=0
    for i in range (1,n+1) :
        if EstPremier(i) :
            s+=1
    return s


import numpy as np
def tab(n):
    L=[]
    for k in range(2,n+1) :
        # L+=[pi(k)]
        L.append(pi(k))
    return np.array(L)

def inverse_log(x):
    return 1/np.log(x)

import scipy.integrate

def Li(x) :
    return scipy.integrate.quad(inverse_log,2,x)[0]

def tabLi(n):
    A=[]
    for k in range(2,n+1) :
        A.append(Li(k))
    return np.array(A)

