class Polynome :
    """
    definition d'une classe polynôme , ou un polynome
    est respresente par la liste des ses coefficients
    """

    def __init__(self,L):
        """ methode constructeur"""
        self.coefs = L
        if L == [0] :
            self.degre = -1
        else :
            self.degre=len(L)-1

    def __repr__(self):
        L=self.coefs
        # p=""
        # for i in range(len(L)) : 
        #     p+= str(L[i]) + 'X^' + str(i) + '+'
        # l=list(p)
        # l.pop()
        # return ''.join(l)
        p=str(L[0]) +'X^' +str(0)
        for i in range(1,len(L)) : 
            p+=  '+' + str(L[i]) + 'X^' + str(i) 
        return p
    
    def __str__(self):
        L=self.coefs
        if L==[0] : 
            p='0'
        else :
            if L[0]!=0 :
                p=str(L[0])
            else :
                p=''
            if L[1]!=0 and L[1]!=1 :
                p+= '+' + str(L[1]) + "X"
            elif L[1]==1 :
                p+= '+' + "X"
            for i in range(2,len(L)):
                if L[i]!=0 and L[i]!=1 :
                    p+= '+' + str(L[i]) + 'X^' + str(i)
                elif L[i]==1 :
                    p+= '+' +  'X^' + str(i)
        return p

    def eval(self,x):
        """Calcule la valeur d'un polynome en x"""
        val = 0
        L=self.coefs
        for i in range(len(L)) :
            val+=L[i] * x**i
        return val

    def eval2(self,x):
        return   sum([self.coefs[i]* x**i for i in range(len(self.coefs))])  

    def Horner(self,x):
        L=self.coefs
        if self.degre == 0 :
            return L[0]
        p=Polynome(L[1:])
        return L[0] + x * p.Horner(x)
    
    import numpy as np
    import matplotlib.pyplot as plt
    def trace(self,xmin,xmax):
        x=np.linspace(xmin,xmax,1000)
        y=[]
        for i in range(1000):
            y+=[self.eval(x[i])]
        plt.plot(x,y)
        plt.show()
        plt.close()
   
class Monome(Polynome) :
    def __init__(self,c,deg):
        L=[0 for i in range(deg) ] + [c]
        Polynome.__init__(self,L)
        self.coef=c
    
    def __str__(self):
        if self.coef !=1 :
            return str(self.coef) + 'X^' + str(self.degre)
        return 'X^' + str(self.degre)
    
    def eval(self,x):
        return self.coef * x **self.degre
    
    def __mul__(self,m2):
        c = self.coef * m2.coef
        d= self.degre + m2.degre

        return Monome(c,d)