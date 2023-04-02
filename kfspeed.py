class KF1():
    def __init__(self,dmove,dsens):
        self.dmove = dmove
        self.dsens = dsens
        self.dtotal = 0
        self.mtotal = 0
        self.k =

    def predict(self,v):
        self.mtotal += v
        self.dtotal += self.dmove
        return self.mtotal,self.dtotal
    def sens(self,v):
        k


