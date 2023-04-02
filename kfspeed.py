class KF1():
    def __init__(self,dmove,dsens):
        self.dmove = dmove**2
        self.dsens = dsens**2
        self.dtotal = 0
        self.mtotal = 0

    def predict(self,v):
        self.mtotal += v
        self.dtotal += self.dmove
        return self.mtotal,self.dtotal
    def sens(self,v):
        k = self.dtotal/(self.dtotal+self.dsens)
        self.dtotal = k*self.dsens
        self.mtotal = self.mtotal + k*(v - self.mtotal)
        return self.mtotal, self.dtotal

#kf = KF1(0.1,0.2)
#print(kf.predict(1))
#print(kf.sens(2))

