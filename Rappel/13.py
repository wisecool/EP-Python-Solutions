def calculsuite1(n):
    u=1
    if n >=1 :
        for i in range(n): # i varie entre 0 et n exclu
            u=3*u +5
    return u

print(calculsuite1(2))

def calculsuite2(n):
    u=1
    l=[]
    if n >=1 :
        for i in range(n): # i varie entre 0 et n exclu
            u=3*u +5
            l.append(u)
    return l


print(calculsuite2(4))