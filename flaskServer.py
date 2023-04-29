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
    data = GPIO.setup(11,GPIO.OUT)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    templateData={
        'title':'Indoor Farm Management - RaspBerry Pi 3 A+',
        'time':timeString,
        'data':data,
        'cpu_percent': psutil.cpu_percent(1),
        'cpu_count': psutil.cpu_count(),
        'cpu_freq': psutil.cpu_freq(),
        'cpu_mem_total': memory.total,
        'cpu_mem_avail': memory.available,
        'cpu_mem_used': memory.used,
        'cpu_mem_free': memory.free,
        'disk_usage_total': disk.total,
        'disk_usage_used': disk.used,
        'disk_usage_free': disk.free,
        'disk_usage_percent': disk.percent,
        'sensor_temperatures': psutil.sensors_temperatures()['cpu-thermal'][0].current,        
    }    
    return render_template('index.html',**templateData)

@app.route('/<actionid>') 
def handleRequest(actionid):
    print("Button pressed : {}".format(actionid))
    return "OK 200"   
                              
if __name__=='__main__':    
    app.run(debug=True, port=5000, host='0.0.0.0',threaded=True)
    #local web server http://192.168.1.200:5000/
    #after Port forwarding Manipulation http://xx.xx.xx.xx:5000/