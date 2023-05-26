#!/usr/bin/env python3

from light import Light
from dht22 import Dht22
from moisture import Moisture
from datetime import datetime
from time import sleep

class Sensor(Light,Dht22,Moisture):

    now = datetime.now().strftime("%H:%M")
    Light.lightOn
    

    def actionRequest(timeON,timeOFF,now,actionid):
        if actionid == 'LightOn':
            Light.light.on()
            return "OK 200" 
        elif actionid == 'LightOff':
            lighton = False 
            Light.light.off()
            return "OK 200"                   
        elif actionid == 'RoutineOn' or actionid == 'RoutineOff':
            if actionid == 'RoutineOn':
                lighton = True
                while lighton:                    
                    if now >= timeON  and now <= timeOFF: 
                        Light.light.on()                    
                    else :
                        Light.light.off()                    
                    sleep(5)
            elif actionid  == 'RoutineOff':
                Light.light.off()
                lighton = False
                return "OK 200"


    def farmBoard():
        global lighton, TentHumidity, TentTemperature    
        board_response = {
        "RoutineOn": Light.lightOn,
        "LightOn": Light.light.is_lit,
        "MoistureOn": Moisture.moisture.is_active,
        "TentTemperature":Dht22.tentTemperature,
        "TentHumidity":Dht22.tentHumidity
        }
        return board_response
    
