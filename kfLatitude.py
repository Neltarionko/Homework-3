class KF1():
    def __init__(self):
        self.dOBD = 0
        self.dGPS = 0
        self.dtotal = 0
        self.mtotal = 0
        self.dmove = 0
        self.a = 0
    def predict(self):
        self.dmove = (0.1 + self.mtotal/10)**2
        self.mtotal += self.a*0.1
        self.dtotal += self.dmove
        #print('d Total',self.dtotal)
        return self.mtotal,self.dtotal**0.5