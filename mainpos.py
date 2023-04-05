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
        x.append(kf.sens(Latitude[k],GPSSpeed[k],Bearing[k]))
    except:
        continue

kf2 = KFy(Longitude[0])
y = []
for k in range(len(GPSTime)):
    kf2.predict()
    y.append(kf2.sens(Longitude[k],GPSSpeed[k],Bearing[k]))

GPSTime = np.array(GPSTime)
x = np.array(x)
pointy2 = np.array([[x[i,0] + x[i,1],x[i,0] - x[i,1]] for i in range(len(GPSTime))])
plt.plot(GPSTime[:]/60 + 18, x[:,0],label='Матожидание текущего положения',color = 'g')
plt.plot(GPSTime[:]/60 + 18,pointy2[:,0],label='дисперсия движения',color = 'm')
plt.plot(GPSTime[:]/60 + 18,pointy2[:,1],color = 'm')
plt.legend()
plt.show()


y = np.array(y)
pointy2 = np.array([[y[i,0] + y[i,1],y[i,0] - y[i,1]] for i in range(len(GPSTime))])
plt.plot(GPSTime[:]/60 + 18, y[:,0],label='Матожидание текущего положения',color = 'g')
plt.plot(GPSTime[:]/60 + 18,pointy2[:,0],label='дисперсия движения',color = 'm')
plt.plot(GPSTime[:]/60 + 18,pointy2[:,1],color = 'm')
plt.legend()
plt.show()


timewidth = 30*1
time = 25
rangeleft = int(((time-18)*60)-timewidth)
rangeright = int(((time-18)*60)+timewidth)
plotx = [GPSTime[i]/60 + 18 for i in range(rangeleft,rangeright)]
ploty = [x[i,0] for i in range(rangeleft,rangeright)]
ploty2 = np.array([[x[i,0] + x[i,1],x[i,0] - x[i,1]] for i in range(rangeleft,rangeright)])
plt.plot(plotx,ploty,label='движение на 25 минуте в течении минутыч',color = 'g')
plt.plot(plotx,ploty2[:,0],label='дисперсия движения',color = 'm')
plt.plot(plotx,ploty2[:,1],color = 'm')
plt.legend()
plt.show()