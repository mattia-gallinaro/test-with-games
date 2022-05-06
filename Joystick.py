import pyfirmata
import time
import flask
import flask_restful
import requests
from time import sleep 
#import numpy
app = flask.Flask("test")

api = flask_restful.Api(app)
data = []
class Data_Joystick:
    def get(self):
        return data
    def post(self):
        return data

try:
    board = pyfirmata.Arduino('COM4')
    it = pyfirmata.util.Iterator(board)
    it.start()
    value_x = board.get_pin('a:0:i')
    value_y = board.get_pin('a:1:i')
    print(value_x.read())
    print(value_y.read())
    while True:
        print("x :")
        print(value_x.read())
        print("y: ")
        print(value_y.read())
        time.sleep(0.32)  
    #with open('log.txt', 'a') as f:
        #f.write('X:'+ value_x.read() +'Y:' + value_y.read() + '\n');
except:
    print("Could't open the port")
    print("Try to plug in your arduino board and try it")
    print("In case it doesn't work even when you have plugged in your board\n try to change the port on the code")

api.add_resource(Data_Joystick)
#url = "http://127.0.0.1:5000"
#response = requests.get(url=url)
#print(response.status_code)
#print(response.text)    
