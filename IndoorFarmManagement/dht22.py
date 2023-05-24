#!/usr/bin/env python3

import Adafruit_DHT as dht
from datetime import datetime
from time import sleep
import plotly.express as px
import pandas as pd

class Dht22:

    ##attributes to read the temperature and humidity in the tent.
    tentHumidity,tentTemperature = dht.read_retry(dht.DHT22,4)    
    tentInfoDF = pd.read_csv('C:\\Users\\leona\\Desktop\\Raspberry Projects\\IndoorFarmManagement\\tentInfoDF.csv')

    def displayTentInfo():    
        global tentInfoDF
        fig = px.line(tentInfoDF, x='time', y='humidity')
        graph_html = fig.to_html(full_html=False)

        with open('/templates/index.html', 'r') as file:
            html_content = file.read()

        updated_html_content = html_content.replace('<!--GRAPH_PLACEHOLDER-->', graph_html)

        with open('/templates/index.html', 'w') as file:
            file.write(updated_html_content)


    ##Method to store the humidity and temperature data in a csv file.        
    def tentInfoDataFrame (tentHumidity,tentTemperature,tentInfoDF): 
        
        while True:
            new_row = {'time': datetime.now(), 'temperature': tentTemperature, 'humidity': tentHumidity}
            tentInfoDF.loc[len(tentInfoDF)] = new_row 
            tentInfoDF.tail(5) 
            tentInfoDF.to_csv('C:\\Users\\leona\\Desktop\\Raspberry Projects\\IndoorFarmManagement\\tentInfoDF.csv', index=False)           
            sleep(600)


