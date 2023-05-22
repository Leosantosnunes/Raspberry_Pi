#!/usr/bin/env python3

from flask import Flask, render_template, request
from datetime import datetime
from os import system  
from gpiozero import LED,DigitalInputDevice,CPUTemperature
import psutil
from time import sleep
import Adafruit_DHT as dht
import plotly.express as px
import pandas as pd
import threading

light = LED(17)
lighton = False 
moisture = DigitalInputDevice(10,pull_up=True)
TentHumidity,TentTemperature = dht.read_retry(dht.DHT22,4)
tentInfoDF = pd.DataFrame(columns=['time', 'temperature', 'humidity'])

def tentInfoDataFrame ():       
    global TentHumidity, TentTemperature,tentInfoDF
      
    while True:
        new_row = {'time': datetime.now(), 'temperature': TentTemperature, 'humidity': TentHumidity}
        tentInfoDF.loc[len(tentInfoDF)] = new_row 
        tentInfoDF.head(5)
        displayTentInfo()
        sleep(600)
        

def displayTentInfo():    
    global tentInfoDF
    fig = px.line(tentInfoDF, x='time', y='humidity')
    graph_html = fig.to_html(full_html=False)

    with open('/templates/index.html', 'r') as file:
        html_content = file.read()

    updated_html_content = html_content.replace('<!--GRAPH_PLACEHOLDER-->', graph_html)

    with open('/templates/index.html', 'w') as file:
        file.write(updated_html_content)

tent_info_thread = threading.Thread(target=tentInfoDataFrame)
tent_info_thread.start()


app=Flask(__name__)
    
@app.route('/')
def index():            
    memory = psutil.virtual_memory()
    temperature = CPUTemperature().temperature
    disk = psutil.disk_usage('/')
    templateData={                        
        'cpu_percent': psutil.cpu_percent(1),        
        'cpu_freq': round(psutil.cpu_freq().current),
        'cpu_mem_total': round((memory.total / 1000000)),        
        'cpu_mem_used': round((memory.used / 1000000)),        
        'disk_usage_total': round((disk.total / 1000000000)),
        'disk_usage_used': round((disk.used / 1000000000)),  
        'sensor_temperatures': round(temperature)        
    }    
    return render_template('index.html',**templateData)

@app.route('/<actionid>',methods = ['POST'])
## manual manipulation of the system
def handleRequest(actionid):
    global lighton     
    timeON = datetime.strptime(request.args.get('timeON'),"%H:%M").strftime("%H:%M")
    timeOFF = datetime.strptime(request.args.get('timeOFF'),"%H:%M").strftime("%H:%M")    
   
    if actionid == 'LightOn':
        light.on()
        return "OK 200" 
    elif actionid == 'LightOff':
        lighton = False 
        light.off()
        return "OK 200"                   
    elif actionid == 'RoutineOn' or actionid == 'RoutineOff':
        if actionid == 'RoutineOn':
            lighton = True
            while lighton:
                now = datetime.now().strftime("%H:%M")
                if now >= timeON  and now <= timeOFF: 
                    light.on()                    
                else :
                    light.off()                    
                sleep(5)
        elif actionid  == 'RoutineOff':
            light.off()
            lighton = False
            return "OK 200"               

    
@app.route('/<farmboard>')
def farm_board(farmboard):
    global lighton, TentHumidity, TentTemperature    
    board_response = {
        "RoutineOn": lighton,
        "LightOn": light.is_lit,
        "MoistureOn": moisture.is_active,
        "TentTemperature":TentTemperature,
        "TentHumidity":TentHumidity
    }
    return board_response

@app.route('/rpi-action/<RPiactionid>',methods = ['POST'])
## manual manipulation of the system
def handleRequestRPi(RPiactionid):        
   
    if RPiactionid == 'rebootbtn':
        system("reboot now -h")
        return 'OK 200'         
    elif RPiactionid == 'shutdownbtn':
        system("shutdown now -h") 
        return 'ok 200' 
                              
if __name__=='__main__':    
    app.run(debug=True, port=5000, host='0.0.0.0',threaded=True)
    #local web server http://192.168.1.61:5000/
    #after Port forwarding Manipulation http://xx.xx.xx.xx:5000/
