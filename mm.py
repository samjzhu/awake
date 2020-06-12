import sys
import time 
import pyautogui 
import random

def move_mouse(intervalSec) :  
    try:
        w,h = pyautogui.size()
        x0, y0 =  pyautogui.position()
        toogle = True
        while True:
            time.sleep(intervalSec)
            x, y =  pyautogui.position()
            if x0 == x and y0 == y : #let's move it if on the same position too long
                x1 = random.randrange(200,w-200)
                y1 = random.randrange(200,h-200)
                try:
                    if(toogle):
                       pyautogui.press('shiftleft')
                    else:
                       pyautogui.press('shiftright')
                    toogle = not toogle
                    pyautogui.moveTo(x1, y1, duration = 1)                           
                except pyautogui.FailSafeException as err:
                    print("FailSafeException[{0},{1}]:{2}!\n".format(x1,y1, err))
                    pyautogui.press('shift')
            x0, y0 =  pyautogui.position()
            print (x0, y0)
    except KeyboardInterrupt:
        print("Game Over!\n") 

def main():
    print("Press ctrl-C to exit!")
    interval = 30 #default to 30 seconds
    if len(sys.argv) > 1: 
        interval = int(sys.argv[1])
    print("interval:", interval)
    move_mouse(interval)

if __name__ == "__main__":
    main()
