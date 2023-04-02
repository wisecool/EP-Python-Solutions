def remplir_fichier(nom_fichier,n):
    f=open(nom_fichier,'w')
    for i in range(n) :
        nom = input("Donner le nom ")
        note = float(input("Donner la note "))
        f.write(nom + ':' + str(note) + '\n')
    f.close()

def remplir_fichier2(nom,n):
    f=open(nom,'w')
    L=[]
    for i in range(n) :
        nom = input("Donner le nom ")
        note = float(input("Donner la note "))
        L.append(nom + ':' + str(note) + '\n')
    f.writelines(L)
    f.close()

# remplir_fichier2('notes',3)

def calculer_moyenne1(nom_fichier):
    f=open(nom_fichier,'r')
    L=f.readlines()
    f.close()
    s=0
    for ch in L :
        e=ch.split(":")
        s+=float(e[1])
    return s/len(L)
def calculer_moyenne2(nom_fichier):
    f=open(nom_fichier,'r')
    s,n=0,0
    while True :
        ch=f.readline(n)
        if ch!='' :
            e=ch.split(':')
            s+=float(e[1])
            n+=1
        else :
            break
    f.close()
    return(s/n)

def calculer_moyenne3(nom_fichier):
    f=open(nom_fichier,'r')
    s,n=0,0
    ch=f.readline()
    while ch!='' :
        e=ch.split(':')
        s+=float(e[1])
        n+=1
        ch=f.readline(n)
    f.close()
    return(s/n)

print(calculer_moyenne3('notes'))

