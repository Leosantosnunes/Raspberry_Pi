#!/usr/bin/env python3

from light import Light
from dht22 import Dht22
from moisture import Moisture
class Sensor(Light,Dht22,Moisture):


    def farmBoard():
        global lighton, TentHumidity, TentTemperature    
        board_response = {
        "RoutineOn": Light.lighton,
        "LightOn": Light.light.is_lit,
        "MoistureOn": Moisture.is_active,
        "TentTemperature":Dht22.TentTemperature,
        "TentHumidity":Dht22.TentHumidity
        }
        return board_response
    