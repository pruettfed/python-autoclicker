import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

#TODO add argument to set delay in command line

#delay bound between 0.01 and 2, default to 0.1
delay = 0.01 #float(sys.argv[0]) if 0.01 <= float(sys.argv[0]) <= 2 else 0.1 
toggle_key = KeyCode(char = "]")
kill_key = KeyCode(char = "k")

print(f"Click delay is set to {delay} seconds")
print(f"Press {toggle_key} to start/stop\nPress {kill_key} to kill the script\n")

clicking = False
program_running = True
mouse = Controller()

def clicker():
    print("called")
    while program_running:
        while clicking:
            mouse.click(Button.left, 1)
        time.sleep(delay)


# class ClickMouse(threading.Thread):
#     def __init__(self, delay):
#         super(ClickMouse, self).__init__()
#         self.delay = delay
#         self.button = Button.left
#         self.running = False
#         self.program_running = True
  
#     def start(self):
#         self.running = True
  
#     def stop(self):
#         self.running = False
  
#     def exit(self):
#         self.stop()
#         self.program_running = False

#     def run(self):
#         while self.program_running:
#             while self.running:
#                 mouse.click(self.button)
#                 time.sleep(self.delay)
#             time.sleep(0.1)
  
# on_press method takes 
# key as argument
def toggle_clicking(key):
    global clicking
    global program_running

    if key == toggle_key:
        if clicking:
            print("paused")
            clicking = False
        else:
            print("started")
            clicking = True
    elif key == kill_key:
        print("killed")
        clicking = False
        program_running = False
        listener.stop()
  
# instance of mouse controller is created
click_thread = threading.Thread(target = clicker)
click_thread.start()

  
with Listener(on_press = toggle_clicking) as listener:
    listener.join()
