from base import *
from kfspeed import *
import matplotlib.pyplot as plt
def main():
    GPSTime, DeviceTime, GPSSpeed, OBDSpeed, Longitude, Latitude, Bearing = values('data1.csv')

    speed = []
    kf = KF1(0.001,0.01,0.02)
    for k in range(len(GPSTime)):
        #('GPS time:',GPSTime[k],'OBD time:',DeviceTime[k*10])
        kf.predict()
        kf.sensGPS(GPSSpeed[k])
        speed.append(kf.sensOBD(OBDSpeed[k*10]))
        for i in range(1,10):
            try:
                kf.predict()
                speed.append(kf.sensOBD(OBDSpeed[k*10+i]))
            except IndexError:
                continue

    speed = np.array(speed)

    plt.plot(DeviceTime, speed[:,0])
    plt.show()

if __name__ == '__main__':
    main()