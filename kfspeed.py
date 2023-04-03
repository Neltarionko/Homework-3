class KF1():
    def __init__(self,dmove,dOBP, dGPS):
        self.dOBD = dOBP ** 2
        self.dGPS = dGPS ** 2
        self.dmove = dmove
        self.dtotal = 0
        self.mtotal = 0
        self.a = 0

    def predict(self):
        self.dtotal += self.a*0.1
        self.dtotal += self.dmove
        #print('d Total',self.dtotal)
        return self.mtotal,self.dtotal**0.5

    def sensGPS(self,v):
        self.a = self.dtotal
        k = self.dtotal/(self.dtotal + self.dGPS)
        #print('k GPS',k)
        self.dtotal = k*self.dGPS
        self.mtotal = self.mtotal + k*(v - self.mtotal)
        self.a -= self.dtotal
        self.a *= -1
        return self.mtotal, self.dtotal**0.5

    def sensOBD(self,v):
        self.a = self.dtotal
        k = self.dtotal/(self.dtotal + self.dOBD+ 0.00000000000001)
        #print('k OBD', k)
        self.dtotal = k*self.dOBD
        self.mtotal = self.mtotal + k*(v - self.mtotal)
        self.a -= self.dtotal
        self.a *= -1
        return self.mtotal, self.dtotal**0.5

    def updatedisp(self, dOBP, dGPS):
        self.dOBD = dOBP ** 2
        self.dGPS = dGPS ** 2

#kf = KF1(0.1,0.2)
#print(kf.predict(1))
#print(kf.sens(2))

