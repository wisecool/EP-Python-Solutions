import random 

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
        
def melange(p1,p2):
    p3=creer_pile()
    while not est_vide(p1) and not est_vide(p2) :
        i= random.randint(1,2)
        if i ==1 :
            empiler(p3,depiler(p1))
        else:
            empiler(p3,depiler(p2))
    
    while not est_vide(p1):
        empiler(p3,depiler(p1))
    
    while not est_vide(p2):
        empiler(p3,depiler(p2))

    return p3

def palindrome(ch):
    p1=creer_pile()
    p2=creer_pile()
    n=len(ch)
    for i in range(n//2):
        empiler(p1,ch[i])
        empiler(p2,ch[-i-1]) # ch[n-1-i]
     
    # for i in range(n//2) :
    while not est_vide(p1) :
        s1=depiler(p1)
        s2=depiler(p2)
        if s1!=s2 :
            return False
    
    return True

def somme_rec(p):
    if taille_pile(p) == 0 :
        return 0
    else :
        s=depiler(p)
        return s+somme_rec(p)



# print(palindrome('LeVel'))

# p1=[1,2,3]
# p2=[5,4]
# print(melange(p1,p2))