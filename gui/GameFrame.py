#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *


class GameFrame(QWidget):
    def __init__(self, parent=None):
        super(GameFrame, self).__init__(parent)
        oImage = QImage("board.png")
        self.main_window()

        sImage = oImage.scaled(QSize(300, 200))  # resize Image to widgets size
        palette = QPalette()
        self.setPalette(palette)

    def main_window(self):
        self.resize(900, 800)
        self.setWindowTitle("Monopoly")
        self.show()
