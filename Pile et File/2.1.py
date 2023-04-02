def creer_file():
    return []

def enfiler(f,e) :
    f.append(e)
    # f.insert(0,'e')

def defiler(f):
    # if not est_vide :
    if  est_vide(f) !=True :
        return f.pop(0)
        # return f.pop()
    else :
        return "File Vide"

def est_vide(f):
    return len(f)==0

def taille_file(f):
    return len(f)

def vider_file(f):
    while est_vide(f)!= True :
        s=defiler(f)
    
def copie_file(f):
    f1=creer_file()
    while not est_vide(f) :
        t=defiler(f)
        enfiler(f1,t)
        enfiler(f,t)
    return f1

def inverser_file(f):
    p=creer_pile()
    f1=copie_file(f)
    while not est_vide(f1):
        t=defiler(f1)
        empiler(p,t)
    while not est_vide(p):
        s=depiler(p)
        enfiler(f1,s)
    return f1

def supp(f,elt):
    while not est_vide(f):
        t=defiler(f)
        if t!=elt :
            enfiler(f,t)
        
def permutation_circulaire(f,k):
    for i in range(k):
        t=defiler(f)
        enfiler(f,t)