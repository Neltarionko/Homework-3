from base import *
from kfLatitude import *
import matplotlib.pyplot as plt

GPSTime, DeviceTime, GPSSpeed, OBDSpeed, Longitude, Latitude, Bearing = values('data1.csv')
kf = KFx(Latitude[0])
x = []
print(len(Bearing))
for k in range(len(GPSTime)):
    try:
        kf.predict()
        x.append(kf.sens(Latitude[k*10],GPSSpeed[k],Bearing[k*10]))
    except:
        continue

kf2 = KFy(Longitude[0])
y = []
for k in range(len(GPSTime)):
    kf2.predict()
    y.append(kf2.sens(Longitude[k*10],GPSSpeed[k],Bearing[k*10]))


x = np.array(x)
pointy2 = np.array([[x[i,0] + x[i,1],x[i,0] - x[i,1]] for i in range(len(GPSTime))])
plt.plot(GPSTime, x[:,0],label='Матожидание текущего положения',color = 'g')
#plt.plot(GPSTime,pointy2[:,0],label='дисперсия движения',color = 'm')
#plt.plot(GPSTime,pointy2[:,1],color = 'm')
plt.show()

y = np.array(y)
pointy2 = np.array([[y[i,0] + y[i,1],y[i,0] - y[i,1]] for i in range(len(GPSTime))])
plt.plot(GPSTime, y[:,0],label='Матожидание текущего положения',color = 'g')
#plt.plot(GPSTime,pointy2[:,0],label='дисперсия движения',color = 'm')
#plt.plot(GPSTime,pointy2[:,1],color = 'm')
plt.show()