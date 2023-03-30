import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    
    def perimetre(self):
        return 2 * math.pi * self.rayon
    
    def surface(self):
        return math.pi * self.rayon ** 2

class Cylindre(Cercle):
    def __init__(self, rayon, hauteur):
        super().__init__(rayon)
        self.hauteur = hauteur
    
    def volume(self):
        return math.pi * self.rayon ** 2 * self.hauteur
    
    def surface(self):
        return 2 * math.pi * self.rayon * self.hauteur + 2 * math.pi * self.rayon ** 2

class Cone(Cercle):
    def __init__(self, rayon, hauteur):
        super().__init__(rayon)
        self.hauteur = hauteur
    
    def volume(self):
        return 1/3 * math.pi * self.rayon ** 2 * self.hauteur
    
    def surface(self):
        l = math.sqrt(self.rayon ** 2 + self.hauteur ** 2)
        return math.pi * self.rayon * (self.rayon + l)

class Sphere(Cercle):
    def volume(self):
        return 4/3 * math.pi * self.rayon ** 3
    
    def surface(self):
        return 4 * math.pi * self.rayon ** 2

c = Cercle(5)
print(f"Le périmètre du cercle de rayon {c.rayon} est {c.perimetre()}")
print(f"La surface du cercle de rayon {c.rayon} est {c.surface()}")

cy = Cylindre(5, 10)
print(f"Le volume du cylindre de rayon {cy.rayon} et de hauteur {cy.hauteur} est {cy.volume()}")
print(f"La surface du cylindre de rayon {cy.rayon} et de hauteur {cy.hauteur} est {cy.surface()}")

cn = Cone(5, 10)
print(f"Le volume du cône de rayon {cn.rayon} et de hauteur {cn.hauteur} est {cn.volume()}")
print(f"La surface du cône de rayon {cn.rayon} et de hauteur {cn.hauteur} est {cn.surface()}")

s = Sphere(5)
print(f"Le volume de la sphère de rayon {s.rayon} est {s.volume()}")
print(f"La surface de la sphère de rayon {s.rayon} est {s.surface()}")
