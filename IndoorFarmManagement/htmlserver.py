#!/usr/bin/env python3

import RPi.GPIO as GPIO
import os
import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
 

host_name = '192.168.1.61'  # IP Address of Raspberry Pi
host_port = 8000


def setupGPIO():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    GPIO.setup(11,GPIO.OUT)


def setLight():
    while True:        
        now = datetime.datetime.now().time()
        ##GPIO.output(11,GPIO.LOW)
        if now.hour >= 7 and now.hour <= 22: 
            return GPIO.output(11,GPIO.HIGH)
        
        else :   
            return GPIO.output(11,GPIO.LOW)
        
def getTemperature():
    temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
    return temp

class MyServer(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _redirect(self, path):
        self.send_response(303)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', path)
        self.end_headers()

    def do_GET(self):
        html = '''
           <html>
           <body 
            style="width:960px; margin: 20px auto;">
           <h1>Welcome to my Raspberry Pi</h1>
           <p>Current GPU temperature is {}</p>
           <form action="/" method="POST">
               Turn Light :
               <input type="submit" name="submit" value="On">
               <input type="submit" name="submit" value="Off">
               Shut Down :
               <input type="submit" name="submit" value="Shut Down">
           </form>
           </body>
           </html>
        '''
        temp = getTemperature()
        self.do_HEAD()
        self.wfile.write(html.format(temp[5:]).encode("utf-8"))

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("utf-8")
        post_data = post_data.split("=")[1]

        setupGPIO()

        if post_data == 'On':
            GPIO.output(11, GPIO.HIGH)
        else:
            GPIO.output(11, GPIO.LOW)

        print("LED is {}".format(post_data))
        self._redirect('/')  # Redirect back to the root url


# # # # # Main # # # # #

if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()