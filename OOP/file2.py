class File:
    def __init__(self):
        self.pile1 = []
        self.pile2 = []

    def enfiler(self, element):
        self.pile1.append(element)

    def defiler(self):
        if not self.pile2:
            if not self.pile1:
                return None
            while self.pile1:
                self.pile2.append(self.pile1.pop())
        return self.pile2.pop()
    def est_vide(self):
        return len(self.pile1) == 0 and len(self.pile2) == 0
    
    def longueur(self):
        return len(self.pile1) + len(self.pile2)

    def sommet(self):
        if len(self.pile2) == 0:
            if len(self.pile1) == 0:
                return None
            while len(self.pile1) > 0:
                tmp = self.pile1.pop()
                self.pile2.append(tmp)
        return self.pile2[-1]