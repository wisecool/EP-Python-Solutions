import random
def fictexte(nom,n):
    f=open(nom,'w')
    for i in range(n) :
        y=random.random()
        ligne=str(y) +'\n' 
        f.write(ligne)
    f.close()

# fictexte('abdallah',20)

def readfile(nom):
    f=open(nom,'r')
    print(type(f.readline()))
    f.close()

readfile('abdallah')