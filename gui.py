from tkinter import *
from main import nimicClass

class nimicMessengerGUI():

    def __init__(self):
        self.window = self.createWindow(400, 300, 500, 540)
        self.createButton(self.window, "Trimite mesajul", "blue", 5, 270)
        self.windowMainLoop(self.window)
        self.nimicObj = nimicClass()

    def createWindow(self, xSize, ySize, xPositionOnScreen, yPositionOnScreen):
        window = Tk()
        window.title('nimicMess by ®CIUTACOOL™')
        window.geometry("400x300+500+540")
        return window

    def createButton(self, window, buttonName, fg, xPosition, yPosition):
        btn = Button(window, text=buttonName, fg=fg)
        btn.place(x=xPosition, y=yPosition)

    def windowMainLoop(self, window):
        window.mainloop()

nimicMessengerGUI()

# window.title('nimicMess by ®CIUTACOOL™')
# window.geometry("400x300+500+540")
# btn=Button(window, text="This is Button widget", fg='blue')
# btn.place(x=5, y=270)
# txtfld=Entry(window, text="This is Entry Widget", bd=5)
# txtfld.place(x=80, y=150)
# lbl=Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
# lbl.place(x=60, y=50)
