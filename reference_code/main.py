import pyttsx3, threading, time, subprocess, platform
from pynput.keyboard import Key, Listener
from tkinter import * 
from tkinter.ttk import *

if __name__ == '__main__':
    def show(key):
        # NOTE: Use a daemon thread to avoid blocking the main thread
        if key == Key.tab:
            print("good")
            threading.Thread(target=lambda:pyttsx3.speak("good"), daemon=True).start() 
            
        if key != Key.tab and key != Key.space and key != Key.delete:
            print("try again")
            threading.Thread(target=lambda:pyttsx3.speak("try again."), daemon=True).start()

        # by pressing 'delete' button 
        # you can terminate the loop 
        if key == Key.delete: 
            return False
        
        # Call floating_window() in the main thread
        if key == Key.space:
            user_msg = "CUSTOM MESSAGE"
            # Run app.py as a separate process to avoid blocking the main thread
            os_name = platform.system()
            if os_name == 'Windows':
                # Using a class for Windows to hide the console window
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW  
                subprocess.Popen(["python", "notify.py", user_msg], startupinfo=startupinfo)
            elif os_name == 'Darwin':
                subprocess.Popen(["python", "notify.py", user_msg], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            elif os_name == 'Linux':
                print('This is a Linux operating system.')
            else:
                print('This is an unknown operating system.')
    
    # Collect all event until released
    with Listener(on_press=show) as listener:
        listener.join()

