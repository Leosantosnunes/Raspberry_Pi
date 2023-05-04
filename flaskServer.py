#!/usr/bin/env python3

from flask import Flask, render_template, Response
import datetime
import os   
import gpiozero
import psutil 



light = gpiozero.LED(17)


app=Flask(__name__)
    
@app.route('/')
def index():    
    now=datetime.datetime.now()
    timeString=now.strftime("%Y-%m-%d %H:%M")    
    memory = psutil.virtual_memory()
    temperature = gpiozero.CPUTemperature().temperature
    disk = psutil.disk_usage('/')
    templateData={
        'title':'Indoor Farm Management - RaspBerry Pi 3 A+',
        'time':timeString,        
        'cpu_percent': psutil.cpu_percent(1),        
        'cpu_freq': round(psutil.cpu_freq().current),
        'cpu_mem_total': round((memory.total / 1000000)),        
        'cpu_mem_used': round((memory.used / 1000000)),        
        'disk_usage_total': round((disk.total / 1000000000)),
        'disk_usage_used': round((disk.used / 1000000000)),  
        'sensor_temperatures': round(temperature)        
    }    
    return render_template('index.html',**templateData)

@app.route('/<actionid>')
## manual manipulation of the system
def handleRequest(actionid):    
    if actionid == 'LightOn':
        light.on()
        return "OK 200" 
    elif actionid == 'LightOff':
        light.off()
        return "OK 200"
        
                   
    elif actionid == 'RoutineOn':
             while True:        
                now = datetime.datetime.now().time()        
                if now.hour >= 7  and now.hour <= 23: 
                    light.on()
                    return "OK 200" 
                else :
                    light.off()
                    return "OK 200"
    elif actionid == 'shutdownbtn':
        return os.system("shutdown now -h") 

##routine of lights ##
# def routine(actionid):
#     while actionid == 'RoutineOff':        
#         now = datetime.datetime.now().time()        
#         if now.hour >= 7 and now.hour <= 23: 
#             return light.on()        
#         else :   
#             return light.off()



                              
if __name__=='__main__':    
    app.run(debug=True, port=5000, host='0.0.0.0',threaded=True)
    #local web server http://192.168.1.61:5000/
    #after Port forwarding Manipulation http://xx.xx.xx.xx:5000/
