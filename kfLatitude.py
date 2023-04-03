class KF2():
    def __init__(self,dOBP, dGPS):
        self.dOBD = dOBP ** 2
        self.dGPS = dGPS ** 2
        self.dtotal = 0
        self.mtotal = 0
        self.dmove = (0.1 + self.mtotal/10)**2
        self.a = 0