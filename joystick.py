import pyfirmata
import time
from time import sleep 
#import numpy
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
    time.sleep(1.0);
    
    #with open('log.txt', 'a') as f:
        #f.write('X:'+ value_x.read() +'Y:' + value_y.read() + '\n');
    
    #x.digital[13].read()
    #time.sleep(1)
    #number = x.digital[14].read()
    #time.wait(10)
    #sleep(10)