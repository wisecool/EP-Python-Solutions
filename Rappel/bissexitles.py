#Q2
annee =int(input('annee'))
if annee % 4 !=0:
    print("Cette année n'est pas bissextile")
elif annee % 100 !=0 :
    print("Cette année est  bissextile")
elif annee % 400 == 0 :
    print("Cette année est  bissextile")
else :
    print("Cette année n'est pas bissextile")

#Q3
def bissextile(annee):
    if(annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
        return True
    return False

    # return annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0

#Q4
compteur =0
for annee in range(10,2015):
    if bissextile(annee) :
        compteur +=1
print(compteur)

def comptage(debut,fin):
    compteur =0
    for annee in range(debut,fin):
        if bissextile(annee) :
            compteur +=1
    return compteur
print(comptage(10,2015))

debut=2023
fin=2024
while comptage(debut,fin) < 200 :
    fin+=1
print(fin-1)