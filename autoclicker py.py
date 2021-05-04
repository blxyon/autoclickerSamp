import time
from datetime import datetime
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode, Key
from pynput.keyboard import Controller as controlla
import random 
delay = 16
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='q')

def getLast():
    f = open("C:\\Users\Valentin\Documents\GTA San Andreas User Files\SAMP\chatlog.txt", "r")
    se=""
    lines=f.readlines()
    for s in lines:
        #print(s.split("]"))
        if(("The roulette landed on RED.") in s):
            se=se+"R"
        elif(("The roulette landed on BLACK.") in s):
            se=se+"B"
        elif(("The roulette landed on GREEN.") in s):
            se=se+"G"
    return se;
def getLastTimeStampLanding():
    f = open("C:\\Users\Valentin\Documents\GTA San Andreas User Files\SAMP\chatlog.txt", "r")
    lastCol="blank"
    lines=[]
    lines=f.readlines()
    for s in lines:
        #print(s)
        if(("The roulette landed on RED.") in s):
            lastCol=s
        elif(("The roulette landed on BLACK.") in s):
            lastCol=s
        elif(("The roulette landed on GREEN.") in s):
            lastCol=s
    print("here1:")
    print(lastCol)
    f.close()
    return(lastCol)
def getLastCol():
    f = open("C:\\Users\Valentin\Documents\GTA San Andreas User Files\SAMP\chatlog.txt", "r")
    
    lastCol="blank"
    lines=f.readlines()
    for s in lines:
        #print(s.split("]"))
        if(("The roulette landed on RED.") in s):
            lastCol="R"
        elif(("The roulette landed on BLACK.") in s):
            lastCol="B"
        elif(("The roulette landed on GREEN.") in s):
            lastCol="G"
    print(lastCol)
    f.close()
    return(lastCol)
class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.bet=10000
        self.permBet=10000
        self.betStreak=0
        self.lasttimeStamp=""
        self.running = False
        self.program_running = True
        self.start_time = time.time()
        

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False
    def updateStreak(self):
        s=getLastTimeStampLanding()
        if(self.lasttimeStamp!=s):
            self.betStreak=self.betStreak+1
            self.bet=self.bet*2+self.permBet
            self.lasttimeStamp=s
            print("new time: ", self.lasttimeStamp)
        
    def run(self):
        while self.program_running:
            while self.running:
                print(getLastCol())
                print("timeLapse: ",time.time()-self.start_time)
                print(getLast())
                if(time.time()-self.start_time>=5400):
                    keyboard.press("t")
                    word="/usedrugs"
                    for l in word:
                        keyboard.press(l)
                        time.sleep(0.15)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)

                    self.start_time=time.time()
                    time.sleep(1)
                    
                elif(getLastCol()=="B"):
                    mouse.click(self.button)
                    time.sleep(random. randint(0,10))
                    suma=(str(self.bet))
                    for l in suma:
                        keyboard.press(l)
                        time.sleep(0.15)
                    self.updateStreak()
                    print(self.bet)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                if(getLastCol()=="R"):
                    self.betStreak=0
                    self.bet=self.permBet
                    mouse.click(self.button)
                    time.sleep(random. randint(0,10))
                    keyboard.press("1")
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                time.sleep(self.delay)
            time.sleep(random. randint(0,10))


mouse = Controller()

keyboard = controlla()
#print(getLastTimeStampLanding())
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        f = open("lasts.txt", "a")
        f.write("\n\n")
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write(dt_string)
        f.write("\n")
        f.write(getLast())
        f.write("\n\n")
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
