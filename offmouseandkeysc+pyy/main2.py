import ctypes, threading, sys, os
from elevate import elevate

elevate(show_console=True)

def relpath(rel):
    return os.path.join(getattr(sys, '_MEIPASS', os.path.abspath(".")), rel)

# mydll = ctypes.CDLL(r"C:\Users\Microsoft\Documents\prrrog\c+pyyy\offmouseandkeysc+pyy\block.dll")
mydll = ctypes.CDLL(relpath("block.dll"))

print("Calling loop_forever()...")
def run_cpp():
    mydll.loop_forever()

# Run in background thread
thread = threading.Thread(target=run_cpp)
thread.start()

i = 0
while (i<1000):
    print(i)
    i+=1