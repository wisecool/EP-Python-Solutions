def moyenne(L) :
    return sum(L)/len(L)
def variance(L):
    m=moyenne(L)
    y=[x**2 - m**2 for x in L]
    return moyenne(y)
