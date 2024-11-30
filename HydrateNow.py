from plyer import notification
import tkinter as tk
import time
import keyboard
import threading
from tkinter import messagebox



def ask_if_working():
    root = tk.Tk()
    root.withdraw()
    response = messagebox.askyesno("Are you working?", "Are you starting with Study/coding?")
    root.quit()
    return response

def send_notification(title, message, timeout, app_name=None, app_icon=None, ticker=None, toast=None):
    notification.notify(
        title=title,
        message=message,
        timeout=timeout
    )
    thread = threading.Thread(target=freeze_screen)
    thread.start()
    thread.join()
    # freeze_screen()     

def freeze_screen():
    root = tk.Tk()
    root.attributes("-fullscreen", True) 
    root.attributes('-topmost', True)     
    root.configure(background='black')

    # Block certain keys
    keyboard.block_key('alt')
    keyboard.block_key('tab')
    keyboard.block_key('win')
    keyboard.block_key('esc')

    # Display the message
    label = tk.Label(
        root,
        text="You must drink water to unlock the screen!",
        fg="white",
        bg="black",
        font=("Arial", 24)
    )
    label.pack(expand=True)
    button = tk.Button(
        root,
        text="I Drank Water",
        command=lambda: unlock_screen(root),
        font=("Arial", 20),
        fg="black",
        bg="white"
    )
    button.pack(pady=20)
    root.mainloop()
    
def unlock_screen(root):
    root.destroy()  
    keyboard.unhook_all()

respone = ask_if_working()
if(respone):
    while(True):
        time.sleep(600)
        send_notification("Hydration Reminder", "It's time to hydrate!", 4)
       
