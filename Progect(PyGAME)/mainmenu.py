import pygame
import sys
from math import pi, cos, sin
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
from tkinter import *
import sqlite3
import os
import glob


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "главное меню"
        self.initUI()
        self.stop = False
        self.w1 = Info()

    def initUI(self):
        label = QLabel(self)
        pixmap = QPixmap('fons/mainmenu.jpg')
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, pixmap.width(), pixmap.height())
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        self.but = QPushButton("1", self)
        self.but.setIcon(QIcon('buttons/new.png'))
        self.but.setIconSize(QSize(500, 140))
        self.but.resize(480, 110)
        self.but.move(1300, 100)
        self.but1 = QPushButton("2", self)
        self.but1.setIcon(QIcon('buttons/vb.png'))
        self.but1.setIconSize(QSize(500, 138))
        self.but1.resize(480, 114)
        self.but1.move(1300, 240)
        self.but2 = QPushButton("3", self)
        self.but2.setIcon(QIcon('buttons/op.png'))
        self.but2.setIconSize(QSize(500, 138))
        self.but2.resize(480, 114)
        self.but2.move(1300, 370)
        self.but3 = QPushButton("4", self)
        self.but3.setIcon(QIcon('buttons/vt.png'))
        self.but3.setIconSize(QSize(500, 138))
        self.but3.resize(480, 114)
        self.but3.move(1300, 520)
        self.but1.installEventFilter(self)
        self.but2.installEventFilter(self)
        self.but3.installEventFilter(self)
        self.but.installEventFilter(self)
        self.but2.clicked.connect(self.open)
        self.but3.clicked.connect(self.open)
        self.but.clicked.connect(self.open)
        self.but1.clicked.connect(self.open)
        self.show()

    def zamen(self, obj):
        if obj.text() == "1":
            if self.stop:
                obj.setIcon(QIcon('buttons/new2.png'))
            else:
                obj.setIcon(QIcon('buttons/new.png'))
        if obj.text() == "2":
            if self.stop:
                obj.setIcon(QIcon('buttons/vb2.png'))
            else:
                obj.setIcon(QIcon('buttons/vb.png'))
        if obj.text() == "3":
            if self.stop:
                obj.setIcon(QIcon('buttons/op2.png'))
            else:
                obj.setIcon(QIcon('buttons/op.png'))
        if obj.text() == "4":
            if self.stop:
                obj.setIcon(QIcon('buttons/vt2.png'))
            else:
                obj.setIcon(QIcon('buttons/vt.png'))

    def eventFilter(self, object, event):
        if event.type() == QEvent.Enter:
            self.stop = True
            self.zamen(object)
            return True
        elif event.type() == QEvent.Leave:
            self.stop = False
            self.zamen(object)
        return False

    def open(self):
        global f
        znak = self.sender().text()
        if znak == "3":
            self.w1.show()
        if znak == "4":
            self.close()
        if znak == "1":
            self.close()
            os.system('python viborcarts.py')


class Info(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "инфо"
        self.initUI()

    def initUI(self):
        label = QLabel(self)
        pixmap = QPixmap('fons/info.jpg')
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, pixmap.width(), pixmap.height())
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        self.but3 = QPushButton("4", self)
        self.but3.setIcon(QIcon('buttons/back.png'))
        self.but3.setIconSize(QSize(500, 138))
        self.but3.resize(480, 110)
        self.but3.move(0, 0)
        self.but3.installEventFilter(self)
        self.but2 = QPushButton("3", self)
        self.but2.setIcon(QIcon('buttons/pravila.png'))
        self.but2.setIconSize(QSize(500, 138))
        self.but2.resize(480, 110)
        self.but2.move(800, 300)
        self.but2.installEventFilter(self)
        self.but = QPushButton("1", self)
        self.but.setIcon(QIcon('buttons/zombytypes.png'))
        self.but.setIconSize(QSize(500, 138))
        self.but.resize(480, 110)
        self.but.move(800, 450)
        self.but.installEventFilter(self)
        self.but1 = QPushButton("2", self)
        self.but1.setIcon(QIcon('buttons/rusttypes.png'))
        self.but1.setIconSize(QSize(500, 138))
        self.but1.resize(480, 110)
        self.but1.move(800, 600)
        self.but1.installEventFilter(self)
        self.but4 = QPushButton("5", self)
        self.but4.setIcon(QIcon('buttons/video.png'))
        self.but4.setIconSize(QSize(500, 138))
        self.but4.resize(480, 110)
        self.but4.move(800, 750)
        self.but4.installEventFilter(self)
        self.but1.clicked.connect(self.open1)
        self.but2.clicked.connect(self.open1)
        self.but.clicked.connect(self.open1)
        self.but3.clicked.connect(self.open1)
        self.but4.clicked.connect(self.open1)


    def zamen(self, obj):
        if obj.text() == "4":
            if self.stop:
                obj.setIcon(QIcon("buttons/back2.png"))
            else:
                obj.setIcon(QIcon("buttons/back.png"))
        if obj.text() == "1":
            if self.stop:
                obj.setIcon(QIcon("buttons/zombytypes2.png"))
            else:
                obj.setIcon(QIcon("buttons/zombytypes.png"))
        if obj.text() == "2":
            if self.stop:
                obj.setIcon(QIcon("buttons/rusttypes2.png"))
            else:
                obj.setIcon(QIcon("buttons/rusttypes.png"))
        if obj.text() == "3":
            if self.stop:
                obj.setIcon(QIcon("buttons/pravila2.png"))
            else:
                obj.setIcon(QIcon("buttons/pravila.png"))
        if obj.text() == "5":
            if self.stop:
                obj.setIcon(QIcon("buttons/video2.png"))
            else:
                obj.setIcon(QIcon("buttons/video.png"))

    def eventFilter(self, object, event):
        if event.type() == QEvent.Enter:
            self.stop = True
            self.zamen(object)
            return True
        elif event.type() == QEvent.Leave:
            self.stop = False
            self.zamen(object)
        return False

    def open1(self):
        znak = self.sender().text()
        if znak == "4":
            self.close()
        if znak == "5":
            os.startfile("pravila.mp4")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())