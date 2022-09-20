### =!= PRUETT.FED =!= ###
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

### =>> PROGRAM VARIABLES <<= ###
clicking = False
program_running = True
mouse = Controller()
version = "1.3.2"

### =>> USER VARIABLES <<= ###
delay = 0.01
toggle_key = KeyCode(char = "p")
kill_key = KeyCode(char = "k")

### |||> MAIN FUNCTION <||| ###
def run():
    print(f"\033[32;1m - Running v{version} of autoclicker - \033[0m\n")
    print(f"Click delay is set to {delay} seconds")
    print(f"Press {toggle_key.char} to start/stop\nPress {kill_key.char} to kill the program\n")

    #create new thread executing main clicking function
    click_thread = threading.Thread(target = clicker)
    click_thread.start()

    #listen for clicking events and trigger keystroke events
    global listener
    with Listener(on_press = toggle_clicking) as listener:
        listener.join()


### |||> AUTOCLICKER <||| ###
def clicker():
    while program_running:
        while clicking:
            mouse.click(Button.left, 1)
            time.sleep(delay)
        time.sleep(0.001) #allow listener to grab keys

### |||> KEYSTROKE EVENTS <||| ###
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
        print("\033[31;1;51m ~ AUTOCLICKER KILLED ~ \033[0m")


if __name__ == "__main__":
    run()