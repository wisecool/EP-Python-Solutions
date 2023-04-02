def espace(ch) :
    for i in range(len(ch)) :
        if  ch[i] == ' ' :
            return i
    return False

def compteur_espace(ch):
    p=0
    for c in ch :
        if  c == ' ' :
            p+=1
    return p
    # list count 

def espacer(ch):
    # if compteur_espace(ch) != 0 :
    #     return ch
    new= ch[0]
    for i in range(1,len(ch)) :
        new += ' ' + ch[i] 
    return new

print(espacer('selmi'))