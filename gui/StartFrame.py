from tkinter import *
from tkinter import messagebox


class StartFrame(object):
    def __init__(self, tokens, players_nicks=[], players_tokens=[]):
        self.tokens = tokens
        self.players_nicks = players_nicks
        self.players_tokens = players_tokens
        self.gui = Tk()
        self.gui.geometry('500x320')
        self.gui.title('Create Players')

        # FRAMES
        self.frame = Frame(self.gui)
        self.frame.pack()
        self.nickFrame = Frame(self.gui)
        self.nickFrame.pack(side=TOP)

        self.players = {}
        self.boardTitle = Label(self.frame, text="Create new player")
        self.boardTitle.config(font=("Calibri", 14))
        self.boardTitleCom = Label(self.frame, text="(2 to 5 players)")
        self.boardTitleCom.config(font=("Calibri", 10))

        self.username = Label(self.nickFrame, text="Nick ")

        self.username.config(font=("Calibri", 10))
        self.getUsername = Text(self.nickFrame, height=1, width=18)
        self.getUsername.config(font=("Calibri", 12))
        self.userToken = Label(self.nickFrame, text=" Token ")
        self.userToken.config(font=("Calibri", 10))
        self.variable = StringVar(self.gui)
        self.variable.set("pick your token")
        self.tokenList = OptionMenu(self.nickFrame, self.variable, *tokens)
        self.tokenList.config(font=("Calibri", 12))
        self.createButton = Button(self.gui, text="Create", width=10, command=lambda: self.get_player())

        self.boardTitle.pack()
        self.boardTitleCom.pack()
        self.username.pack(side=LEFT)
        self.getUsername.pack(side=LEFT)
        self.userToken.pack(side=LEFT)
        self.tokenList.pack()
        self.createButton.pack()

        # MENU
        self.menubar = Menu(self.gui)

        self.startMenu = Menu(self.menubar, tearoff=0)
        self.startMenu.add_command(label="Close", command=lambda: self.gui.destroy())
        self.menubar.add_cascade(label="Menu", menu=self.startMenu)

        self.gui.config(menu=self.menubar)

        self.gui.mainloop()

    def get_player(self):
        nick = self.getUsername.get("1.0", "end-1c")
        token = self.variable.get()
        if len(nick) < 2 or ' ' in nick:
            message = "This nick is too short"
            not_player(message)
        elif nick in self.players_nicks:
            message = "This nick is already used"
            not_player(message)
        elif token in self.players_tokens:
            message = "This token is already used"
            not_player(message)
        elif token == "pick your token":
            message = "Pick your token"
            not_player(message)
        else:
            self.players_nicks.append(nick)
            self.players_tokens.append(token)
            self.getUsername.delete("1.0", END)
            self.show_players()

    def show_players(self):
        i = len(self.players_nicks) - 1

        show = ("{} is {}".format(self.players_nicks[i], self.players_tokens[i]))
        display = Label(self.gui, text=show)
        display.config(font=("Calibri", 12))
        display.pack()

        if i == 1:
            start_button = Button(self.gui, text="Start game", width=10, command=lambda: self.gui.destroy())
            start_button.pack(side=BOTTOM)


def not_player(bad):
    messagebox.showinfo("!!!", bad)
