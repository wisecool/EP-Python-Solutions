 def creer_pile():
	return[]

def empiler(P,e):
	P.append(e)	

def depiler(P):
	assert est_vide(P)!=True, "vous depilez a partir d'une pile vide"
	return P.pop()
	

def est_vide(P):
	return len(P)==0

def taille_pile(P):
	return len(P)

def vider_pile(P):
	while (est_vide(P)!=True):
		s=depiler(P)

def bien_parenthese(ch):
    p=creer_pile()
    for i in range(len(ch)):
	    if ch[i] =='(' or ch[i] =='{' or ch[i] =='[' :
		    empiler(p,ch[i])
		else:
            try:
                s=depiler(P)
                if s=='(' and i!=')':
                    return False
                elif s=='{' and i!='}':
                    return False
                elif s=='[' and i!=']':
                    return False
                                
            except:
                return False
	return est_vide(p)
    