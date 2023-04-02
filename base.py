# Библиотеки

import numpy as np
import pandas as pd

# Функция для получения данных

def values(csv):
    # Открытие файла
    df = pd.read_csv(csv, delimiter=',', header=None, skiprows=1,  names=['GPS Time', 'Device Time', 'Longitude', 'Latitude',
       'GPS Speed (Meters/second)', 'Horizontal Dilution of Precision',
       'Altitude', 'Bearing', 'G(x)', 'G(y)', 'G(z)', 'G(calibrated)',
       'Engine RPM(rpm)', 'Speed (OBD)(km/h)', 'Acceleration Sensor(Total)(g)',
       'Litres Per 100 Kilometer(Instant)(l/100km)', 'Speed (GPS)(km/h)',
       'Acceleration Sensor(Z axis)(g)'])
    df.tail()
    df['Speed (GPS)(km/h)'] = df['Speed (GPS)(km/h)'].replace('-','-1',regex=True)
    df.dropna()

    # Обработка

    GPSTime_prep = np.array(df['GPS Time'])
    DeviceTime_prep = np.array(df['Device Time'])
    GPSSpeed = np.array(df['Speed (GPS)(km/h)'],dtype = 'float')
    OBDSpeed = np.array(df['Speed (OBD)(km/h)'],dtype = 'float')
    Longitude = np.array(df['Longitude'],dtype = 'float')
    Latitude = np.array(df['Latitude'],dtype = 'float')
    Bearing = np.array(df['Bearing'],dtype = 'float')

    GPSTime = []
    DeviceTime = []

    GPSTime.append(0)
    for i in range (1, len(GPSTime_prep),10):
        GPSTime.append(i)

    for i in range (len(DeviceTime_prep)):
        DeviceTime.append(i)

    # Итоговые данные

    #print(GPSTime) #время с GPS
    #print(DeviceTime) #время с устройства
    #print(GPSSpeed) #скорость с GPS
    #print(OBDSpeed) #скорость с бортовой диагностики
    #print(Longitude) #долгота
    #print(Latitude) #широта
    #print(Bearing) #горизонтальный угол между устройством и севером
    
    return GPSTime, DeviceTime, GPSSpeed, OBDSpeed, Longitude, Latitude, Bearing

# Вызов функции

#GPSTime, DeviceTime, GPSSpeed, OBDSpeed, Longitude, Latitude, Bearing = values('data1.csv')