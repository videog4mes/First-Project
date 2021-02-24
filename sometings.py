import ctypes

user_handle = ctypes.WinDLL("User32.dll") # Used for handeling graphical data and other stuff
k_handle = ctypes.WinDLL("Kernel32.dll") # Used for interacting with processes, file systems , and threads.
 

hWnd = None
lpText = "Hello World"
lpCaption = "Hussein Muhaisen"
uType = 0x00000001

response = user_handle.MessageBoxW(hWnd, lpText,lpCaption, uType) # W --> Strings 
error = k_handle.GetLastError()
if error !=0:
    print("Error Code: (0)".format(error))
    exit(1)

if response == 1:
    print("User Clicked OK")
elif response == 2:
    print("User Clicked Cancel!")
    
