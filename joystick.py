from curses import baudrate
from socket import timeout
import pyfirmata
import serial
import importlib.util
import time
import flask
import serial
#import flask_restful
import requests
import sys
from time import sleep 
#spec = importlib.util.spec_from_file_location("pyfirmata", "/home/mattia/.local/lib/python3.9/site-packages/pyfirmata/__init__.py")
#foo = importlib.util.module_from_spec(spec)
#spec.loader.exec_module(foo)
#spec2 = importlib.util.spec_from_file_location("pyfirmata", serial.__file__)
#fo2 = importlib.util.module_from_spec(spec2)
#spec.loader.exec_module(fo2)
#foo.()
#print(sys.path)
print(pyfirmata.__file__)
#import numpy
app = flask.Flask("test")

#api = flask_restful.Api(app)
data = []
class Data_Joystick:
    def get(self):
        return data
    def post(self):
        return data


try:
        board = pyfirmata.Arduino("/dev/ttyACM0")
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

#app.add_resource(Data_Joystick)
if __name__ == "__main__":
    #app.flask.run()
    print("I can start the program")
#if _main_ =="_main_":
#    app.run()

#url = "http://127.0.0.1:5000"
#response = requests.get(url=url)
#print(response.status_code)
#print(response.text)    
