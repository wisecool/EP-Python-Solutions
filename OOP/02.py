class Duree :
    def __init__(self,t=(0,0)):
        # assert type(t) == tuple
        self.minute=t[0]
        self.seconde=t[1]
    def __repr__(self):
        """
        methode d'affichage d'une duree sous la forme mm min ss s
        """
        return  "{} min {} s".format(self.minute,self.seconde)
        # return  "{min} min {sec} s".format(min=self.minute,sec=self.seconde)

    def __add__(self,d):
        s= (self.seconde + d.seconde) % 60
        m=  self.minute + d.minute + (self.seconde + d.seconde) // 60

        return Duree((m,s))



d=duree((20,30))
print(d)
