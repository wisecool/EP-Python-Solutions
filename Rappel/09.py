def test(x,L):
    for i in range(len(L)) :
        if L[i] == x :
            return i
    return False