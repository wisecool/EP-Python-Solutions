def  palindrome(ch):
    """
    fonction booleene qui renvoie True si ch est un palindrome ,False sinon
    """
    n= len(ch)
    i=0
    while i < n//2 :
        # if ch[i] != ch[n-1-i] :
        if ch[i] != ch[-1-i] :
            return False
        i+=1
    return True