def creer_pile():
    return []

def empiler(p,e):
    p.append(e)

def depiler(p):
    assert est_vide(p) != True , "vous depilez á partir d'une pile vide"
    # return p.pop(-1)
    return p.pop()

def est_vide(p) :
    return len(p) == 0

def taille_pile(p) :
    return len(p)

def vider_pile(p):
    while (est_vide(p) != True) :
        s = depiler(p)

def afficher_pile(p):
    for i in range(len(p)-1,-1,-1):
        print(p[i])

def copier_pile(p) :
    pi=creer_pile()
    pc=creer_pile()
    while(est_vide(p) != True) :
        sommet=depiler(p)
        empiler(pi,sommet)
    while not est_vide(pi) :
        s=depiler(pi)
        empiler(pc,s)
        empiler(p,s)

    return pc

p=[1,2,3]
print(afficher_pile(p))
print(id(copier_pile(p))== id(p))