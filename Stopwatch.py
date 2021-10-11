import tkinter 
from tkinter import *
import time
import threading
root = Tk()
root.title("Stopwatch")
root.geometry("600x200")

sec=0;min=0;hr=0;stp=0
counting = False
def start():
    global sec,min,hr
    global counting,label1
    counting = True
    while counting:
        sec += 1
        if sec == 60:
            sec = 0
            min = min + 1
        elif min == 60:
            hr = hr + 1
            min = 0
        label1["text"] = "%i:%i:%i"%(hr,min,sec)
        time.sleep(1) 

def stop():
    global stp
    global counting
    counting = False
    stp = 1
def reset():
    global sec,min,hr
    global counting,label1
    counting = False
    sec=0;min=0;hr=0
    label1["text"] = "%i:%i:%i"%(hr,min,sec)

def close():
    root.destroy()

Top = Frame(root, width=600)
Top.pack(side=TOP)
Bottom = Frame(root, width=600)
Bottom.pack(side=BOTTOM)
Start = Button(Bottom, text='Start',width=20, height=2, command=lambda:threading.Thread(target=start,daemon=True).start())
Start.pack(side=LEFT)
Stop = Button(Bottom, text='Stop',width=20, height=2, command=stop)
Stop.pack(side=LEFT)
Reset = Button(Bottom, text='Reset',width=20, height=2, command=reset)
Reset.pack(side=LEFT)
Exit = Button(Bottom, text='Close',width=20, height=2,command=close)
Exit.pack(side=LEFT)
Title = Label(Top, text="Stopwatch by Cejai", font=("Ariel", 25), fg="white", bg="black")
Title.pack(fill=X)
label1 = Label(root, text="%i:%i:%i"%(hr,min,sec),font=("arial", 30, "bold"),foreground = "red", background="black", width = 10);label1.pack()
root.config(bg="black")

root.mainloop()