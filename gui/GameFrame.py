import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap


class GameFrame(QWidget):
    def __init__(self):
        super().__init__()
        # self.players = players
        self.title = 'Monopoly'
        self.width = 1100
        self.height = 900
        self.left = 30
        self.top = 50

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.init_board()
        self.show_players()
        self.show()

    def init_board(self):

        label = QLabel(self)
        pixmap = QPixmap('board.png')
        label.setPixmap(pixmap)
        label.setGeometry(self.left, self.top, pixmap.width(), pixmap.height())
        print("allll")
        self.show()

    def show_players(self):
        pass


def create_frame():
    # if __name__ == '__main__':
    #     app = QApplication(sys.argv)
    # sys.exit(app.exec_())
    #
    # return ex
    pass

GameFrame()

# create_frame()
