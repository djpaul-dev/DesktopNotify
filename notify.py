import pyttsx3, time, sys, threading
from tkinter import * 
from tkinter.ttk import *


def bar(floating_window, p_bar):
    """Function to show the progress bar"""  
    p_label = StringVar()
    p_label.set("Doing dummy work...")
  
    # Show Progress Label
    Label(floating_window, textvariable = p_label, font = ('Helvetica', 12)).pack(pady = 10)

    # Progress bar value updation
    p_bar['value'] = 50
    floating_window.update_idletasks()
    time.sleep(0.5)

    p_bar['value'] = 100
    floating_window.update_idletasks()
    time.sleep(0.5)

    # Change the message of the label
    p_label.set("Done!!")
    time.sleep(1)

    # Destroy the floating window
    floating_window.destroy()

def on_button_click(floating_window, progress):
    """Function to handle button click event"""
    threading.Thread(target=bar, args=(floating_window, progress), daemon=True).start()
    pyttsx3.speak('Pretending to do something...')

if __name__ == '__main__':
    # Take first argument as the message
    message = sys.argv[1]
    
    # Speaking the message
    # engine = pyttsx3.init()
    pyttsx3.speak('You have a new message!')

    # Create the floating window
    floating_window = Tk()
    floating_window.geometry('+650+350')
    floating_window.wm_overrideredirect(True)
    floating_window.title('Floating Window')
    
    # Keep the window always on top
    floating_window.attributes('-topmost', True)
    
    # Message label
    Label(floating_window, text="⚠️ Alert!", font=('Helvetica', 12)).pack(pady=10, padx=10)
    Label(floating_window, text=message, font=('Helvetica', 12)).pack(pady=0, padx=0)
    
    # Start Button
    p_bar = Progressbar(floating_window, orient=HORIZONTAL, length=200, mode='determinate')  # Progress bar widget
    Button(floating_window, text='Click Me!', command=lambda:on_button_click(floating_window, p_bar)).pack(pady=10)
    p_bar.pack(pady=10) # Pack the progress bar widget

    # infinite loop
    floating_window.mainloop()



