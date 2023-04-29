#!/usr/bin/env python3

from flask import Flask, render_template, Response
import datetime
import os
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)


app=Flask(__name__)
    
@app.route('/')
def index():
    #return 'hello world!'
    now=datetime.datetime.now()
    timeString=now.strftime("%Y-%m-%d %H:%M")
    data = GPIO.setup(11,GPIO.OUT)
    templateData={
        'title':'Indoor Farm Management - RaspBerry Pi 3 A+',
        'time':timeString,
        'data':data,
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