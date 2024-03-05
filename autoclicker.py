from tkinter import *
import pyautogui as gui
import threading
from pynput.keyboard import Listener, KeyCode
from time import sleep
win = Tk()
win.geometry('500x300')
win.resizable(False, False)
win.title('AutoClicker Config Window')
L, R, D = 'n', 'm', 1

def update(event, T):
    if event.keysym.isalnum():
        T.delete(0, END)
        T.insert(0, event.keysym)

LCT = Entry(win, width=20, justify='center', font=(20))
LCT.place(x=5, y=5)
L1 = Label(win, text='Left Click', font=(18))
L1.place(x=270, y=5)
RCT = Entry(win, width=20, justify='center', font=(20))
RCT.place(x=5, y=75)
L2 = Label(win, text='Right Click', font=(18))
L2.place(x=270, y=75)
DCT = Entry(win, width=20, justify='center', font=(20))
DCT.place(x=5, y=145)
L3 = Label(win, text='Delay (in milliseconds)', font=(18))
L3.place(x=270, y=145)
LCT.bind('<KeyRelease>', lambda e: update(e, LCT))
RCT.bind('<KeyRelease>', lambda e: update(e, RCT))

def sub(event):
    global L, R, D
    if len(LCT.get()) == 1:
        L = LCT.get()
    if len(RCT.get()) == 1:
        R = RCT.get()
    if len(DCT.get()) != 0:
        D = DCT.get()
    win.destroy()
    
SUB = Button(win, text='Submit', font=(18))
SUB.place(x=200, y=250)
SUB.bind('<Button-1>', sub)

win.mainloop()

class Click(threading.Thread):
    def __init__(self):
        super(Click, self).__init__()
        self.l = 0
        self.r = 0
        try:
            self.d = float(D)/1000
        except:
            self.d = 1/1000

    def Left(self):
        self.l = not self.l
        self.r = 0

    def Right(self):
        self.l = 0
        self.r = not self.r

    def run(self):
        while True:
            sleep(self.d)
            if self.l:
                gui.click()
            if self.r:
                gui.click(button='secondary')

M = Click()
M.start()


def rel(key):
    if key == KeyCode.from_char(L):
        M.Left()
        print('Toggled Left click')
    if key == KeyCode.from_char(R):
        M.Right()
        print('Toggled Right click')

with Listener(on_release=rel) as l:
    l.join()
