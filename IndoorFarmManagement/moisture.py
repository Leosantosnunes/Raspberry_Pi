#!/usr/bin/env python3

from gpiozero import DigitalInputDevice
class Moisture:

    moisture = DigitalInputDevice(10,pull_up=True)





