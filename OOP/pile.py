class Pile:
    #Méthode constructeur
    def __init__(self, L):
        self.liste = L
    def __repr__(self) :
    # Méthode affichage
        s='sommet\n'
        for elt in self.liste :
            s+='||' + str(elt) + '||\n'
        s+='Bas'
        return s
    
     def empiler(self,e):
        self.liste.append(e)
        # self.liste.insert(0,e)
    def depiler(self):
        self.liste.pop()
        # self.liste.pop(0)
        # del self.liste[0]
    def sommet(self):
        return self.liste[-1]
        # return self.liste[0]
    def est_pile_vide(self):
        # return self.liste == []
        return len(self.liste) == 0
    def hauteur(self):
        return len(self.liste)
    
    def pop(self):
        # return self.depiler()
        # a=self.liste[-1]
        # del a
        # return a
        return self.liste.pop()

# Créer un objet Pile avec une liste initiale d'éléments
pile = Pile([1, 2, 3])


# Ajouter un nouvel élément à la pile
pile.empiler(4)

# Afficher le contenu de la pile
pile.afficheur()

# Dépiler l'élément en haut de la pile
sommet = pile.depiler()
print("Elément en haut de la pile :", sommet)

# Afficher le contenu de la pile
pile.afficheur()

# Vérifier si la pile est vide
print("La pile est-elle vide ? :", pile.estVide())

# Obtenir la hauteur de la pile
print("Hauteur de la pile :", pile.hauteur())

# Obtenir l'élément en haut de la pile sans le supprimer
sommet = pile.sommet()
print("Elément en haut de la pile :", sommet)

# Dépiler l'élément en haut de la pile en utilisant la méthode pop()
sommet = pile.pop()
print("Elément en haut de la pile :", sommet)

# Afficher le contenu de la pile
pile.afficheur()
