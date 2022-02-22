import pyfirmata;
import time;

x = [1,2,3,4,5,6,7,8,9,1];

anchor = pyfirmata.Arduino()
it =  pyfirmata.INPUT

def write() :
  time.wait(25)
  while True:
    x = anchor.board[10].input()
    write(x)   

y = anchor.board[11].input()
    write
