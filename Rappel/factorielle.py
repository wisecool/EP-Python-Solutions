def fact(n) :
    prod =1
    if n >1 :
        for i in range(1,n):
           prod *= (i+1)
    return prod   

print(fact(5))