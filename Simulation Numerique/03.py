def F(x):
    # if 0<= x< 1 :
    if x >=0 and x <1 :
        return x
    elif  1<=x <2 :
        return 1
    else :
        return 0
# q2
import mathplotlib.pyplot as plt
n=200 # nombre de points
x=[i*0.01 for i in range(n) ]
y=[]
# for elt in x :
for i in range(n) :
    # y.append(F(elt))
    y.append(F(x[i]))

plt.figure()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphe y=f(x)')
plt.plot(x,y)
plt.ylim(0,1.5)
plt.show()
