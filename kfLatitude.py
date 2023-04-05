import math
class KFx():
    def __init__(self,mtotalpos):
        self.dspeed = 0
        self.dpos =  0.00001
        self.dtotalpos = 0.00001
        self.dtotalspeed = 0
        self.mtotalpos = mtotalpos
        self.mtotalspeed = 0
        self.v = 0
        self.a = 0

    def predict(self):
        self.mtotalspeed += self.a
        self.mtotalpos += (self.mtotalspeed + self.a / 2)/85.4
        self.dtotalspeed += (0.0000000000000000000000000000001 + self.mtotalspeed / 10) ** 2
        self.dtotalpos += self.dtotalspeed/85.4
        return self.mtotalpos, self.dtotalpos**0.5, self.mtotalspeed, self.dtotalspeed**0.5

    def sens(self,x,v,angl):
        v = v*math.sin(angl*3.14/180)
        self.a = self.v
        self.v = self.mtotalpos
        if v == -1:
            self.dspeed = 99999999999
        else:
            self.dspeed = v/10
        k = self.dtotalpos / (self.dtotalpos + self.dpos)
        self.dtotalpos = k * self.dpos
        self.mtotalpos = self.mtotalpos + k * (x - self.mtotalpos)
        k = self.dtotalspeed / (self.dtotalspeed + self.dspeed)
        self.dtotalspeed = k * self.dspeed
        self.mtotalspeed = (self.mtotalspeed + k * (v - self.mtotalspeed))
        self.v -= self.mtotalpos
        self.v *= -1
        self.a -= self.v
        self.a *= -1
        return self.mtotalpos, self.dtotalpos ** 0.5, self.mtotalspeed, self.dtotalspeed ** 0.5

class KFy():
    def __init__(self,mtotalpos):
        self.dspeed = 0
        self.dpos = 0.00001
        self.dtotalpos = 0.00001
        self.dtotalspeed = 0
        self.mtotalpos = mtotalpos
        self.mtotalspeed = 0
        self.v = 0
        self.a = 0

    def predict(self):
        self.mtotalspeed += self.a
        self.mtotalpos += (self.mtotalspeed + self.a / 2)/111.3
        self.dtotalspeed += (0.0000000000000000000000000000001 + self.mtotalspeed / 10) ** 2
        self.dtotalpos += self.dtotalspeed/111.3
        return self.mtotalpos, self.dtotalpos**0.5, self.mtotalspeed, self.dtotalspeed**0.5

    def sens(self,x,v,angl):
        v = v*math.cos(angl*3.14/180)
        self.a = self.v
        self.v = self.mtotalpos
        if v == -1:
            self.dspeed = 99999999999999
        else:
            self.dspeed = v/10
        k = self.dtotalpos / (self.dtotalpos + self.dpos)
        self.dtotalpos = k * self.dpos
        self.mtotalpos = self.mtotalpos + k * (x - self.mtotalpos)
        k = self.dtotalspeed / (self.dtotalspeed + self.dspeed)
        self.dtotalspeed = k * self.dspeed
        self.mtotalspeed = (self.mtotalspeed + k * (v - self.mtotalspeed))
        self.v -= self.mtotalpos
        self.v *= -1
        self.a -= self.v
        self.a *= -1
        return self.mtotalpos, self.dtotalpos ** 0.5, self.mtotalspeed, self.dtotalspeed ** 0.5

