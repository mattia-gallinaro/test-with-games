from asyncio.windows_events import NULL
from logging import NullHandler
import pyfirmata
import threading
import time
import flask

board  = NULL
it = NULL
value_x  = NULL
value_y = NULL
app = flask.Flask(__name__)
try:
    board = pyfirmata.Arduino
    it = pyfirmata.util.Iterator(board)
    it.start()
    value_x = board.get_pin('a:0:i')
    value_y = board.get_pin('a:1:i')
except:
    print("Could'n find the port maybe")
    print("Try to run application with sudo")

def Send_Data():
    print(value_x.read())
    print(value_y.read())
    data = NULL
    data = value_y.read()
    return data

for i in 2:
    t = threading.Thread(target = Send_Data() args())
    t.start()
    t.join()