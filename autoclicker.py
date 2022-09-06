### =!= WORK IN PROGRESS =!= ###
# TODO: see if you can get listener inside run function
# TODO: add CLI tools like flags for delay/key/etc.
# TODO: move formatting from bash script to here on process killed
# TODO: create executable version
# TODO: dockerize environment and create package

import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

### =>> PROGRAM VARIABLES <<= ###
clicking = False
program_running = True
mouse = Controller()

### =>> USER VARIABLES <<= ###
delay = 0.01
toggle_key = KeyCode(char = "p")
kill_key = KeyCode(char = "k")

### |> MAIN FUNCTION <| ###
def run():
    print(f"Click delay is set to {delay} seconds")
    print(f"Press {toggle_key} to start/stop\nPress {kill_key} to kill the program\n")

    #create new thread targeting main clicking function
    click_thread = threading.Thread(target = clicker)
    click_thread.start()


def clicker():
    while program_running:
        while clicking:
            mouse.click(Button.left, 1)
            time.sleep(delay)

#event triggered by listener
def toggle_clicking(key):
    global clicking
    global program_running

    #if toggle key is pressed -> invert the value of clicking bool
    #if kill key is pressed -> terminate program
    if key == toggle_key: clicking = not clicking
    elif key == kill_key:
        clicking = False
        program_running = False
        listener.stop()

if __name__ == "__main__":
    run()

#listen for clicking events 
with Listener(on_press = toggle_clicking) as listener:
    listener.join()