#!/usr/bin/env python3

from gpiozero import LED

class Light:

    light = LED(17)
    lighton = False