from tkinter import *
from nimicClassFile import nimicClass


class nimicMessengerGUI(nimicClass):

    def __init__(self):
        self.window = self.createWindow(400, 300, 500, 540)
        self.message = StringVar()
        self.labelName = StringVar()
        self.labelObject = self.addLabel(self.window, 60, 150)
        self.addTextBox(self.window, "", 80, 150)
        self.createButton(self.window, "Trimite mesajul", 5, 100)
        self.windowMainLoop(self.window)

    def createWindow(self, xSize, ySize, xPositionOnScreen, yPositionOnScreen):
        window = Tk()
        window.title('nimicMess by ®CIUTACOOL™')
        window.geometry(xSize.__str__() + "x" + ySize.__str__() +
                        '+' + xPositionOnScreen.__str__() +
                        '+' + yPositionOnScreen.__str__())
        return window

    def createButton(self, window, buttonName, xPosition, yPosition):
        btn = Button(window, text=buttonName, fg='blue', command=lambda: self.sendMessage())
        btn.place(x=xPosition, y=yPosition)
        btn.pack()

    def addTextBox(self, window, labelName, xPosition, yPosition, bd=5):
        Entry(window, text=labelName, textvariable=self.message).pack()

    def addLabel(self, window, xPosition, yPosition, fg='red'):
        lbl = Label(window, text="text liber", fg='red', font=("Helvetica", 16))
        lbl.place(x=xPosition, y=yPosition)
        lbl.pack()
        return lbl

    def windowMainLoop(self, window):
        window.mainloop()

    def readMessage(self):
        '''
        Reads the message from the input
        :return: textbox text variable
        '''
        return self.message.get()

    def encodeMessage(self, uncodedMessage):
        return nimicClass().encryptMessage(uncodedMessage)

    def decodeMessage(self, encodedMessage):
        return nimicClass().decryptMessage(encodedMessage)

    def sendMessage(self):
        self.writeMessageToLabel(self.readMessage())
        return (self.encodeMessage(self.readMessage()))

    def receiveMessage(self, message):
        nimicClass().decryptMessage(message)

    def writeMessageToLabel(self, message):
        self.labelObject['text'] = message

nimicMessengerGUI()
