#!/usr/bin/env python3

from flask import Flask, render_template, request
from datetime import datetime
from time import sleep
import plotly.express as px
import pandas as pd
import threading
import sensor
import rPiHardware


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
    sensor.templateData    
    return render_template('index.html',**sensor.templateData)

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
def handleRequest2(farmboard):
    sensor.Sensor.farmBoard()


@app.route('/rpi-action/<RPiactionid>',methods = ['POST'])
## manual manipulation of the system
def handleRequestRPi(RPiactionid):        
   rPiHardware.RPihardware(RPiactionid)
                              
if __name__=='__main__':    
    app.run(debug=True, port=5000, host='0.0.0.0',threaded=True)
    #local web server http://192.168.1.61:5000/
    #after Port forwarding Manipulation http://xx.xx.xx.xx:5000/
