from math import pi

def volume(r):
    return 4/3*pi*r**3

def couronne(r,R):
    if r<=R :
        return pi*R**2 -pi*r**2
    else :
        return "la couronne n'existe pas "