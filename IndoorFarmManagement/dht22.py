#!/usr/bin/env python3

import Adafruit_DHT as dht
from datetime import datetime
from time import sleep
import plotly.express as px
import pandas as pd

class Dht22:

    ##attributes to read the temperature and humidity in the tent.
    tentHumidity,tentTemperature = dht.read_retry(dht.DHT22,4)    
    tentInfoDF = pd.read_csv('/home/leonardo/Desktop/shared/tentInfoDF.csv')

    

    ##Method to store the humidity and temperature data in a csv file.        
    def tentInfoDataFrame(self):        
        while True:
            
            now = datetime.now()            
            new_row = {'time': now, 'temperature': self.tentTemperature, 'humidity': self.tentHumidity}
            self.tentInfoDF.loc[len(self.tentInfoDF)] = new_row 
            self.tentInfoDF.tail(5) 
            self.tentInfoDF.to_csv('/home/leonardo/Desktop/shared/tentInfoDF.csv', index=False)           
            sleep(600)


