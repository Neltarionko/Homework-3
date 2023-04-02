from base import *
from kfspeed import *
import matplotlib.pyplot as plt

GPSTime, DeviceTime, GPSSpeed, OBDSpeed, Longitude, Latitude, Bearing = values('data1.csv')

kf = KF1(0.1,0.2)
print(len(GPSTime),len(DeviceTime))
for k in range(len(GPSTime)):
    print('GPS time:',GPSTime[k],'OBD time:',DeviceTime[k*10])
    for i in range(9):
        DeviceTime[1+i]
        #print(kf.sens(1+i))
    #print(kf.predict(OBDSpeed[11]))
    #print(kf.sens(GPSSpeed[1]))