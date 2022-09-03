# import getopt/argparser
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

#TODO add argument to set delay in command line
#TODO I should probably make a bash execute script so I don't need to worry about venv/args

#delay bound between 0.01 and 2, default to 0.1
delay = 0.01#float(sys.argv[0]) if 0.01 <= float(sys.argv[0]) <= 2 else 0.1 
print(f"Delay is {delay} seconds")

button = Button.left
start_stop_key = KeyCode(char = "]")
kill_key = KeyCode(char = "k")

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
  
    def start_clicking(self):
        self.running = True
  
    def stop_clicking(self):
        self.running = False
  
    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)
  
  
# instance of mouse controller is created
mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()
  
  
# on_press method takes 
# key as argument
def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
              
    elif key == kill_key:
        click_thread.exit()
        listener.stop()
  
  
with Listener(on_press=on_press) as listener:
    listener.join()
