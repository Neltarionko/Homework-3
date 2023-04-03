from base import *
from kfspeed import *
import matplotlib.pyplot as plt
def main():
    GPSTime, DeviceTime, GPSSpeed, OBDSpeed, Longitude, Latitude, Bearing = values('data1.csv')
    dGPS = 30
    dOBD = 30
    speed = []
    kf = KF1(dOBD,dGPS)
    for k in range(len(GPSTime)):
        dGPS = GPSSpeed[k]/10
        dOBD = OBDSpeed[k*10]/10
        if (k - 15)//60 >= 25-18 and (k - 15)//60 <= 35-18:
            kf.updatedisp(dOBD,999999999999999)
        if (k - 15)//60 >= 40-18 and (k - 15)//60 <= 50-18:
            kf.updatedisp(999999999999999,dGPS)
        if (k - 15)//60 >= 35-18 and (k - 15)//60 <= 40-18 or (k - 15)//60 >= 50-18:
            kf.updatedisp(dOBD, dGPS)
        #('GPS time:',GPSTime[k],'OBD time:',DeviceTime[k*10])
        kf.predict()
        kf.sensGPS(GPSSpeed[k])
        speed.append(kf.sensOBD(OBDSpeed[k*10]))
        for i in range(1,10):
            try:
                dGPS = GPSSpeed[k] / 10
                dOBD = OBDSpeed[k*10+i] / 10
                if (k - 15) // 60 >= 25 - 18 and (k - 15) // 60 <= 35 - 18:
                    kf.updatedisp(dOBD, 999999999999999)
                if (k - 15) // 60 >= 40 - 18 and (k - 15) // 60 <= 50 - 18:
                    kf.updatedisp(999999999999999, dGPS)
                if (k - 15) // 60 >= 35 - 18 and (k - 15) // 60 <= 40 - 18 or (k - 15) // 60 >= 50 - 18:
                    kf.updatedisp(dOBD, dGPS)
                    kf.predict()
                speed.append(kf.sensOBD(OBDSpeed[k*10+i]))
            except IndexError:
                continue

    speed = np.array(speed)


    pointx = [DeviceTime[i]/60 + 18 for i in range(0,len(DeviceTime),600)]
    pointy = [[speed[i,0] + speed[i,1],speed[i,0] - speed[i,1]] for i in range(0,len(DeviceTime),600)]
    pointy2 = [speed[i,0] for i in range(0,len(DeviceTime),600)]
    plt.plot(pointx, pointy2)
    plt.plot(pointx,pointy)
    plt.show()

if __name__ == '__main__':
    main()