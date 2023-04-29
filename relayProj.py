import RPi.GPIO as GPIO
import datetime
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)

try:
    while True:        
        now = datetime.datetime.now().time()
        ##GPIO.output(11,GPIO.LOW)
        if now.hour >= 7 and now.hour <= 22: 
            GPIO.output(11,GPIO.HIGH)
        
        else :   
            GPIO.output(11,GPIO.LOW)
                
finally:
    GPIO.cleanup()
        
