def appartient(mot,ch):
    """
        fonction booléenne qui renvoie True si mot est dans la chaine
        False sinon
    """
    i = 0
    n=len(ch)
    p= len(mot)
    while  i <= n-p :
        if ch[i:i+p] == mot :
            return True
        i += 1
    return False


print(appartient('mi','selmi'))

