def compteur(L) :
    c = 0
    for x in L :
        if x != 0 :
            c += 1
    return c 

print(compteur([0,0,0,0]))