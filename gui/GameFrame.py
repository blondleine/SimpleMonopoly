from tkinter import *


class GameFrame(object):
    def __init__(self):
        self.gui = Tk()
        self.gui.geometry('700x700')
        self.gui.title('Monopoly')

        # FRAMES
        self.frame = Frame(self.gui)
        self.frame.pack()

        self.boardTitle = Label(self.frame, text="Create new player")
        self.boardTitle.config(font=("Calibri", 14))
        self.boardTitleCom = Label(self.frame, text="(2 to 5 players)")
        self.boardTitleCom.config(font=("Calibri", 10))

        # MENU
        self.menubar = Menu(self.gui)

        self.startMenu = Menu(self.menubar, tearoff=0)
        self.startMenu.add_command(label="Close", command=lambda: self.gui.destroy())
        self.menubar.add_cascade(label="Menu", menu=self.startMenu)

        self.gui.config(menu=self.menubar)

        self.gui.mainloop()