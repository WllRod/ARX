import ctypes
import sys
from os.path import basename

def return_message(text, error):
    cod = 0x40
    if(error):
        cod = 0x10
    ctypes.windll.user32.MessageBoxW(0, text, basename(sys.argv[0]), cod)
