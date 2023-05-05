#!/usr/bin/env python3

from flask import Flask, render_template, request
from datetime import datetime
import os   
import gpiozero
import psutil 



light = gpiozero.LED(17)
now = datetime.now().time().strftime("%H:%M") 


app=Flask(__name__)
    
@app.route('/')
def index():            
    memory = psutil.virtual_memory()
    temperature = gpiozero.CPUTemperature().temperature
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

@app.route('/<actionid>')
## manual manipulation of the system
def handleRequest(actionid):
    timeON = datetime.strptime(request.args.get('timeON'),"%H:%M").strftime("%H:%M")
    timeOFF = datetime.strptime(request.args.get('timeOFF'),"%H:%M").strftime("%H:%M")    
   
    if actionid == 'LightOn':
        light.on()
        return "OK 200" 
    elif actionid == 'LightOff':
        light.off()
        return "OK 200"                   
    elif actionid == 'RoutineOn' or actionid == 'RoutineOff':
        print(now)
        print(timeON)
        print(timeOFF)
        while True:                      
            if now >= timeON  and now <= timeOFF: 
                light.on()
                return "OK 200"
            else :
                light.off()
                return "OK 200"
    elif actionid == 'shutdownbtn':
        return os.system("shutdown now -h") 
                              
if __name__=='__main__':    
    app.run(debug=True, port=5000, host='0.0.0.0',threaded=True)
    #local web server http://192.168.1.61:5000/
    #after Port forwarding Manipulation http://xx.xx.xx.xx:5000/
