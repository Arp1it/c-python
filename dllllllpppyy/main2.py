import ctypes, threading

mydll = ctypes.CDLL(r"C:\Users\Microsoft\Documents\prrrog\c+pyyy\dllllllpppyy\myfunctions2.dll")

def run_cpp():
    mydll.long_running_function()

# Run in background thread
thread = threading.Thread(target=run_cpp)
thread.start()

print("Python is still running while C++ works!")
print("Python is still running while C++ works!")
print("Python is still running while C++ works!")
