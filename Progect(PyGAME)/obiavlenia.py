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


con = sqlite3.connect("levelcarts.db")
cur = con.cursor()
i = cur.execute("Select name from cartslevels WHERE id=?", (1,)).fetchall()
i = i[0][0]
b = cur.execute("Select level from cartslevels WHERE name=?", (i,)).fetchall()
d = cur.execute("Select carts from cartslevels WHERE name=?", (i,)).fetchall()
d = d[0][0].split(">")
b = b[0][0]
if b == 1:
    znach = 1
con.commit()
con.close()


class Level2(QWidget):
    def __init__(self, a, b):
        super().__init__()
        self.lvl = a
        self.name = b
        self.title = "инфо"
        self.initUI()

    def initUI(self):
        label = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        pixmap = QPixmap('fons/kj.jpg')
        if self.lvl == 1:
            pixmap2 = QPixmap('rust/potato.png')
        pixmap3 = QPixmap('buttons/potato.png')
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, pixmap.width(), pixmap.height())
        label2.move(250, 110)
        label3.move(100, 310)
        label.setPixmap(pixmap)
        label2.setPixmap(pixmap2)
        label3.setPixmap(pixmap3)
        self.but = QPushButton("1", self)
        self.but.setIcon(QIcon('buttons/ponal.png'))
        self.but.setIconSize(QSize(500, 138))
        self.but.resize(230, 90)
        self.but.move(450, 490)
        self.but.installEventFilter(self)
        self.resize(pixmap.width(), pixmap.height())
        self.but.clicked.connect(self.save)
        self.show()

    def zamen(self, obj):
        if obj.text() == "1":
            if self.stop:
                obj.setIcon(QIcon('buttons/ponal2.png'))
            else:
                obj.setIcon(QIcon('buttons/ponal.png'))

    def eventFilter(self, object, event):
        if event.type() == QEvent.Enter:
            self.stop = True
            self.zamen(object)
            return True
        elif event.type() == QEvent.Leave:
            self.stop = False
            self.zamen(object)
        return False

    def save(self):
        con = sqlite3.connect("levelcarts.db")
        cur = con.cursor()
        cur.execute("UPDATE cartslevels SET level = ? WHERE name = ?", (self.lvl, self.name), ).fetchall()
        con.commit()
        con.close()
        pygame.quit()
        self.close()
        os.system('python viborcarts.py')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Level2(b, i)
    sys.exit(app.exec_())