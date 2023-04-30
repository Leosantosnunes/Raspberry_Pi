#!/usr/bin/env python3

from flask import Flask, render_template, Response
import datetime
import os
import RPi.GPIO as GPIO
import psutil 


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)


app=Flask(__name__)
    
@app.route('/')
def index():    
    now=datetime.datetime.now()
    timeString=now.strftime("%Y-%m-%d %H:%M")    
    memory = psutil.virtual_memory()
    temperature = psutil.sensors_temperatures()['cpu-thermal'][0].current
    disk = psutil.disk_usage('/')
    templateData={
        'title':'Indoor Farm Management - RaspBerry Pi 3 A+',
        'time':timeString,        
        'cpu_percent': psutil.cpu_percent(1),        
        'cpu_freq': psutil.cpu_freq(),
        'cpu_mem_total': memory.total,        
        'cpu_mem_used': memory.used,        
        'disk_usage_total': disk.total,
        'disk_usage_used': disk.used,  
        'sensor_temperatures': temperature        
    }    
    return render_template('index.html',**templateData)

@app.route('/<actionid>') 
def handleRequest(actionid):
    print("Button pressed : {}".format(actionid))
    if actionid == 'LightOn':
        return GPIO.output(11,GPIO.HIGH)
    elif actionid == 'LightOff':
        return GPIO.output(11,GPIO.LOW)
    elif actionid == 'shutdownbtn':
        return os.system("shutdown now -h")


                              
if __name__=='__main__':    
    app.run(debug=True, port=5000, host='0.0.0.0',threaded=True)
    #local web server http://192.168.1.200:5000/
    #after Port forwarding Manipulation http://xx.xx.xx.xx:5000/