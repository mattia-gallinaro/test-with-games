import importlib.util
import serial

spec = importlib.util.spec_from_file_location("serial", serial.__file__)
fo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fo)

if __name__ == "__main__" :
    try:
        board= fo.Serial("/dev/ttyACM0", 9600, 0 ,True)
        print("I can read from the arduino port")
        value_x = board.get_pin("a:0:i")
        while True: 
            print(value_x)
    except:
        print("That would be so nice if it worked")