import multiprocessing
import os
import pyfirmata
import serial 
#import flask
#from json import jsonify
from flask import Flask, request, jsonify
data =[]
incomes = [{ 'description': 'salary', 'amount': 5000 }]
try:
    board = pyfirmata.Arduino('/dev/ttyACM0')
    it = pyfirmata.util.Iterator(board)
    value_x = board.get_pin('a:0:i')
    value_y = board.get_pin('a:1:i')
except:
    print("This wont't work if you don't plug in Port")
    exit(1)

def f(x):
    print(x*x)

def app():
    app_f = Flask(__name__)
    app_f.run()

@app.route(route='/data', methods= ['GET'])
def incomes():
    jsonify(incomes)
    return 0

@app.route(route='/data', methods=['POST'])
def Loading():
    incomes.append(request.json())
    return '', 204

def ArduinoRead():
    data.append(value_x.read())
    data.append(value_y.read())


p_Arduino = multiprocessing.Process(target = ArduinoRead(), args=())
p_Flask = multiprocessing.Process(target = app(), args= ())
p = multiprocessing.Process(target = f, args = (3, ))
p.start()
p.join()

with multiprocessing.Pool(5) as e:
    print(e.map(f, [1,2,3]))
