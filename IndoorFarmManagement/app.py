#!/usr/bin/env python3

from flask import Flask, render_template
import threading
from sensor import Sensor
import rPiHardware


tent_info_thread = threading.Thread(target=Sensor.tentInfoDataFrame)
tent_info_thread.start()


app=Flask(__name__)
    
@app.route('/')
def index():    
    Sensor.templateData    
    return render_template('index.html',**Sensor.templateData)

@app.route('/<actionid>',methods = ['POST'])
## manual manipulation of the system
def handleRequest(actionid):            
    Sensor.actionRequest(Sensor.lighton,Sensor.timeON,Sensor.timeOFF,Sensor.now,actionid)
    
@app.route('/<farmboard>')
def handleRequest2(farmboard):
    Sensor.farmBoard()


@app.route('/rpi-action/<RPiactionid>',methods = ['POST'])
## manual manipulation of the system
def handleRequestRPi(RPiactionid):        
   rPiHardware.RPihardware(RPiactionid)
                              
if __name__=='__main__':    
    app.run(debug=True, port=5000, host='0.0.0.0',threaded=True)
    #local web server http://192.168.1.61:5000/
    #after Port forwarding Manipulation http://xx.xx.xx.xx:5000/
