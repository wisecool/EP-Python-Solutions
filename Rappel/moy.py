from math import sqrt
def moyenne(L) :
    
    # la fonction retourne la moyenne des elements de L
    n= len(L)
    som = 0
    for i in range(n) :  
    # i varie entre 0 et n-1
        som = som + L[i]  
    # 2 methode
    # for elt  in L :
    #     som = som + elt

    moy = som / n
    return moy

def moyenne2 (L):
    return sum(L) /len(L)

def ecart_type(L) :
    moy=moyenne(L)
    som = 0
    n=len(L)
    for elt in L :
        som = som + (elt - moy)**2
    return sqrt(som/n)
    
def moy(L:list) -> float :
    # la fonction retourne la moyenne(flaot) des elements de la liste L
    assert type(L)== list
    assert len(L) > 0

    som = 0
    n=len(L)
    for i in range(n) :
        assert type(L[i])==float or type(L[i])==int
        som+=L[i] 
        #som = som + L[i]
    som = som /n

    return som

L=[13.2,12.1,12.1,13.2]

print(moyenne(L))
print(moy(L))
# print(ecart_type(L))

