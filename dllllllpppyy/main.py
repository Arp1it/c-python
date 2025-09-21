import ctypes

# Load with full absolute path
mydll = ctypes.CDLL(r"C:\Users\Microsoft\Documents\prrrog\c+pyyy\dllllllpppyy\myfunctions.dll")

# If you have add function
mydll.add.argtypes = [ctypes.c_int, ctypes.c_int]
mydll.add.restype = ctypes.c_int
print("Add Result:", mydll.add(5, 10))

# If you have hello function
mydll.hello()

# cl /LD /EHsc main.cpp /Fe:myfunctions.dll