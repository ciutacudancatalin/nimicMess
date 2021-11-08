from tkinter import *
from main import nimicClass


class nimicMessengerGUI():

    def __init__(self):
        self.window = self.createWindow(400, 300, 500, 540)
        self.createButton(self.window, "Trimite mesajul", 5, 100)
        self.message = StringVar()
        self.addTextBox(self.window, "", 80, 150)
        self.windowMainLoop(self.window)
        self.nimicClassObj = nimicClass()

    def createWindow(self, xSize, ySize, xPositionOnScreen, yPositionOnScreen):
        window = Tk()
        window.title('nimicMess by ®CIUTACOOL™')
        window.geometry(xSize.__str__() + "x" + ySize.__str__() +
        '+' + xPositionOnScreen.__str__() +
        '+' + yPositionOnScreen.__str__())
        return window

    def createButton(self, window, buttonName, xPosition, yPosition):
        btn = Button(window, text=buttonName, fg='blue', command=lambda: self.receiveMessage())
        btn.place(x=xPosition, y=yPosition)

    def addTextBox(self, window, labelName, xPosition, yPosition, bd=5):
        Entry(window, text=labelName, textvariable=self.message).grid(row=0, column=1, sticky=E)

    def windowMainLoop(self, window):
        window.mainloop()

    def readMessage(self):
        '''
        Reads the message from the input
        :return: textbox text variable
        '''
        return self.message.get()

    def encodeMessage(self, uncodedMessage):
        return self.nimicClassObj.encryptMessage(uncodedMessage)

    def decodeMessage(self, encodedMessage):
        return self.nimicClassObj.decryptMessage(encodedMessage)

    def sendMessage(self):
        return (self.encodeMessage(self.readMessage()))

    def receiveMessage(self):
        print(self.decodeMessage(self.sendMessage()))

    def readMessageToConsole(self):
        print(self.readMessage())


nimicMessengerGUI()

# window.title('nimicMess by ®CIUTACOOL™')
# window.geometry("400x300+500+540")
# btn=Button(window, text="This is Button widget", fg='blue')
# btn.place(x=5, y=270)
# txtfld=Entry(window, text="This is Entry Widget", bd=5)
# txtfld.place(x=80, y=150)
# lbl=Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
# lbl.place(x=60, y=50)
