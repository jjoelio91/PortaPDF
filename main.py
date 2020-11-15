from tkinter import *

from Controllers.PasswordEncryptController import PasswordEncryptController

def window_manager():

    root = Tk(className='PortaPDF')

    password_encrypt_view = PasswordEncryptController(root)

    root.mainloop()

if __name__ == "__main__": 
    window_manager()