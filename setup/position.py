
from pynput.mouse import Listener

POSITIONS=[]



def on_click(x, y, button, pressed):
    global POSITIONS   
    pos = (x,y)
    if pressed:
        POSITIONS.append(pos)
    print('{0} at {1}'.format('Pressed' if pressed else 'released', pos))
    
    if len(POSITIONS) == 3:
        return False
        # Stop listener
        

print("You have three clicks 1:open your browser 2:click join now/ask to join 3:click leave meet")
        
with Listener(on_click=on_click) as listener:
    listener.join()


file=open("coordinates.py", "w")

file.write("COORDINATES="+str(POSITIONS[1:])+"\n")

file.close()

print(POSITIONS)