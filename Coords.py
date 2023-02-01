import keyboard 
from pynput import mouse
def get_coords(x, y):
    print("Now at: {}".format((x, y)))
    
with mouse.Listener(on_move = get_coords) as listen:
   
    keyboard.add_hotkey('esc', listen.stop)
    listen.join()
