import webbrowser
from pynput.mouse import Listener

POSITIONS=[]


webbrowser.open_new("https://www.google.com/")

def on_click(x, y, button, pressed):
    global POSITIONS   
    pos = (x,y)
    if pressed:
        POSITIONS.append(pos)
    print('{0} at {1}'.format('Pressed' if pressed else 'released', pos))
    
    if len(POSITIONS) == 3:
        return False
        # Stop listener
        


        
with Listener(on_click=on_click) as listener:
    listener.join()


file=open("coordinates.py", "w")

file.write("coordinates="+str(POSITIONS)+"\n")

file.close()

print(POSITIONS)