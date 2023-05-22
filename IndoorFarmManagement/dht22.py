#!/usr/bin/env python3

import Adafruit_DHT as dht
class Dht22:

    ##attributes to read the temperature and humidity in the tent.
    TentHumidity,TentTemperature = dht.read_retry(dht.DHT22,4)

