#!/usr/bin/env python3

import psutil
from os import system 
from gpiozero import CPUTemperature

class RPihardware():

    Rpiaction = ''
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

    def RequestRPi(RPiactionid):        
   
        if RPiactionid == 'rebootbtn':
            system("reboot now -h")
            return 'OK 200'         
        elif RPiactionid == 'shutdownbtn':
            system("shutdown now -h") 
            return 'ok 200' 
