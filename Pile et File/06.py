from pile import * 

def notation_polonaise(L):
	P=creer_pile()
	try:	
		for i in L:
			if i=='+':
				a=depiler(P)
				b=depiler(P)
				empiler(P,a+b)
			elif i=='*':
				a=depiler(P)
				b=depiler(P)
				empiler(P,a*b)
			else:
				empiler(P,i)
		if taille_pile(P)!=1:
			#pour gerer le cas d'une pile comportant 1 2 sans operateur
			return 'Expression invalide'
	
		else:
			res=depiler(P)
			return(res)
	except:
		#pour gerer le cas où on depile a partir d'une pile vide c'est la fonction depiler
		#qui genere l'erreur avec pop
		return 'Expression invalide: depilement a partir de pile vide'
        
print(notation_polonaise([2,3,'*','+']))