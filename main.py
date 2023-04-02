from base import *
from kfspeed import *

GPSTime, DeviceTime, GPSSpeed, OBDSpeed, Longitude, Latitude, Bearing = values('data1.csv')

kf = KF1(0.1,0.2)

print(kf.predict(OBDSpeed[0]))
print(kf.sens(GPSSpeed[0]))
print(GPSTime[0])
print(DeviceTime[0])
for i in range(9):
    print(DeviceTime[1+i])
    print(kf.sens(1+i))
print(kf.predict(OBDSpeed[11]))
print(kf.sens(GPSSpeed[1]))
print(GPSTime[1])
print(DeviceTime[10])