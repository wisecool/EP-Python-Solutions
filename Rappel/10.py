def somme(L):
    s=0
    for i in range(len(L)) :
       s+= L[i]
    return s

def maximum(L):
    m=L[0]  # initialisation de m
    for elt in L[1:] :
        if elt > m : # si on trouve une valeur plus grande que m
            m=elt  # on la met dans m
    return m

def minimum(L) :
    m=L[0]  # initialisation de m
    for elt in L[1:] :
        if elt < m : # si on trouve une valeur plus grande que m
            m=elt  # on la met dans m
    return m

print(minimum([1,4,3,6,12,34,5]))
print(maximum([1,4,3,6,12,34,5]))
print(somme([1,4,3,6,12,34,5]))

