#!/usr/bin/env python3

from flask import Flask, render_template,request
import threading
from sensor import Sensor, Dht22
from rPiHardware import RPihardware
from datetime import datetime


dht22_instance = Dht22()  # Create an instance of the Dht22 class
tent_info_thread = threading.Thread(target=dht22_instance.tentInfoDataFrame)
tent_info_thread.start()


app=Flask(__name__)
    
@app.route('/')
def index():    
    RPihardware.templateData    
    return render_template('index.html',**RPihardware.templateData)

@app.route('/<actionid>',methods = ['POST'])
## manual manipulation of the system
def handleRequest(actionid):
    timeON = datetime.strptime(request.args.get('timeON'),"%H:%M").strftime("%H:%M")
    timeOFF = datetime.strptime(request.args.get('timeOFF'),"%H:%M").strftime("%H:%M")           
    return Sensor.actionRequest(timeON,timeOFF,Sensor.now,actionid)
    
@app.route('/<farmboard>')
def handleRequest2(farmboard):
    return Sensor.farmBoard()


@app.route('/rpi-action/<RPiactionid>',methods = ['POST'])
## manual manipulation of the system
def handleRequestRPi(RPiactionid):
    print(RPiactionid)       
    return RPihardware.RequestRPi(RPiactionid)
                              
if __name__=='__main__':    
    app.run(debug=True, port=5000, host='0.0.0.0',threaded=True)
    #local web server http://192.168.1.61:5000/
    #after Port forwarding Manipulation http://xx.xx.xx.xx:5000/
