from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5 import uic


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(977, 764)
        self.fon = QtWidgets.QPushButton(Form)
        self.fon.setGeometry(QtCore.QRect(-50, -50, 1000, 1000))
        self.fon.setText("")
        self.fon.setObjectName("fon")
        self.fon2 = QtWidgets.QPushButton(Form)
        self.fon2.setGeometry(QtCore.QRect(580, 100, 371, 531))
        self.fon2.setText("")
        self.fon2.setObjectName("fon2")
        self.foto = QtWidgets.QPushButton(Form)
        self.foto.setGeometry(QtCore.QRect(600, 120, 331, 231))
        self.foto.setText("")
        self.foto.setObjectName("foto")
        self.opis = QtWidgets.QPushButton(Form)
        self.opis.setGeometry(QtCore.QRect(600, 370, 331, 241))
        self.opis.setText("")
        self.opis.setObjectName("opis")
        self.vihod = QtWidgets.QPushButton(Form)
        self.vihod.setGeometry(QtCore.QRect(30, 700, 100, 30))
        self.vihod.setText("")
        self.vihod.setObjectName("vihod")
        self.tekst = QtWidgets.QPushButton(Form)
        self.tekst.setGeometry(QtCore.QRect(180, -3, 650, 90))
        self.tekst.setText("")
        self.tekst.setObjectName("tekst")
        self.pushButton_01 = QtWidgets.QPushButton(Form)
        self.pushButton_01.setGeometry(QtCore.QRect(30, 160, 100, 150))
        self.pushButton_01.setText("")
        self.pushButton_01.setObjectName("pushButton_01")
        self.pushButton_02 = QtWidgets.QPushButton(Form)
        self.pushButton_02.setGeometry(QtCore.QRect(160, 160, 100, 150))
        self.pushButton_02.setText("")
        self.pushButton_02.setObjectName("pushButton_02")
        self.pushButton_03 = QtWidgets.QPushButton(Form)
        self.pushButton_03.setGeometry(QtCore.QRect(290, 160, 100, 150))
        self.pushButton_03.setText("")
        self.pushButton_03.setObjectName("pushButton_03")
        self.pushButton_04 = QtWidgets.QPushButton(Form)
        self.pushButton_04.setGeometry(QtCore.QRect(420, 160, 100, 150))
        self.pushButton_04.setText("")
        self.pushButton_04.setObjectName("pushButton_04")
        self.pushButton_05 = QtWidgets.QPushButton(Form)
        self.pushButton_05.setGeometry(QtCore.QRect(30, 330, 100, 150))
        self.pushButton_05.setText("")
        self.pushButton_05.setObjectName("pushButton_05")
        self.pushButton_06 = QtWidgets.QPushButton(Form)
        self.pushButton_06.setGeometry(QtCore.QRect(160, 330, 100, 150))
        self.pushButton_06.setText("")
        self.pushButton_06.setObjectName("pushButton_06")
        self.pushButton_07 = QtWidgets.QPushButton(Form)
        self.pushButton_07.setGeometry(QtCore.QRect(290, 330, 100, 150))
        self.pushButton_07.setText("")
        self.pushButton_07.setObjectName("pushButton_07")
        self.pushButton_08 = QtWidgets.QPushButton(Form)
        self.pushButton_08.setGeometry(QtCore.QRect(420, 330, 100, 150))
        self.pushButton_08.setText("")
        self.pushButton_08.setObjectName("pushButton_08")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        uic.loadUi('opis.ui', self)
        self.pushButton_01.clicked.connect(self.odi)
        self.pushButton_02.clicked.connect(self.dva)
        self.pushButton_03.clicked.connect(self.tri)
        self.pushButton_04.clicked.connect(self.che)
        self.pushButton_05.clicked.connect(self.pat)
        self.pushButton_06.clicked.connect(self.she)
        self.pushButton_07.clicked.connect(self.sem)
        self.pushButton_08.clicked.connect(self.vos)
        self.vihod.clicked.connect(self.navihod)

        self.a = 0

        self.pushButton_01.setIconSize(QSize(100, 150))
        self.pushButton_01.setIcon(QIcon('zombies/icon/zom1_icon.jpg'))
        self.pushButton_02.setIconSize(QSize(100, 150))
        self.pushButton_02.setIcon(QIcon('zombies/icon/zom2_icon.jpg'))
        self.pushButton_03.setIconSize(QSize(100, 150))
        self.pushButton_03.setIcon(QIcon('zombies/icon/zom3_icon.jpg'))
        self.pushButton_04.setIconSize(QSize(100, 150))
        self.pushButton_04.setIcon(QIcon('zombies/icon/zom4_icon.jpg'))
        self.pushButton_05.setIconSize(QSize(100, 150))
        self.pushButton_05.setIcon(QIcon('zombies/icon/zom5_icon.jpg'))
        self.pushButton_06.setIconSize(QSize(100, 150))
        self.pushButton_06.setIcon(QIcon('zombies/zom6.jpg'))
        self.pushButton_07.setIconSize(QSize(100, 150))
        self.pushButton_07.setIcon(QIcon('zombies/zom7.jpg'))
        self.pushButton_08.setIconSize(QSize(100, 150))
        self.pushButton_08.setIcon(QIcon('zombies/zom8.jpg'))

        self.fon2.setIconSize(QSize(1000, 1000))
        self.fon2.setIcon(QIcon('zombies/fon2.jpg'))
        self.fon.setIconSize(QSize(1600, 1600))
        self.fon.setIcon(QIcon('zombies/fon1.jpg'))

        self.opis.setIconSize(QSize(331, 241))
        self.opis.setIcon(QIcon('zombies/opisanie/none.jpg'))
        self.foto.setIconSize(QSize(331, 241))
        self.foto.setIcon(QIcon('zombies/opisanie/none.jpg'))

    def odi(self):
        self.foto.setIconSize(QSize(250, 300))
        self.foto.setIcon(QIcon('zombies/zom1.jpg'))
        self.opis.setIconSize(QSize(331, 241))
        self.opis.setIcon(QIcon('zombies/opisanie/opis1.jpg'))

    def dva(self):
        self.foto.setIconSize(QSize(250, 300))
        self.foto.setIcon(QIcon('zombies/zom2.jpg'))
        self.opis.setIconSize(QSize(331, 241))
        self.opis.setIcon(QIcon('zombies/opisanie/opis2.jpg'))

    def tri(self):
        self.foto.setIconSize(QSize(250, 300))
        self.foto.setIcon(QIcon('zombies/zom3.jpg'))
        self.opis.setIconSize(QSize(331, 241))
        self.opis.setIcon(QIcon('zombies/opisanie/opis3.jpg'))

    def che(self):
        self.foto.setIconSize(QSize(250, 300))
        self.foto.setIcon(QIcon('zombies/zom4.jpg'))
        self.opis.setIconSize(QSize(331, 241))
        self.opis.setIcon(QIcon('zombies/opisanie/opis4.jpg'))

    def pat(self):
        self.foto.setIconSize(QSize(250, 300))
        self.foto.setIcon(QIcon('zombies/zom5.jpg'))
        self.opis.setIconSize(QSize(331, 241))
        self.opis.setIcon(QIcon('zombies/opisanie/opis5.jpg'))

    def she(self):
        self.foto.setIconSize(QSize(250, 300))
        self.foto.setIcon(QIcon('zombies/zom6.jpg'))
        self.opis.setIconSize(QSize(331, 241))
        self.opis.setIcon(QIcon('zombies/opisanie/opis6.jpg'))

    def sem(self):
        self.foto.setIconSize(QSize(250, 300))
        self.foto.setIcon(QIcon('zombies/zom7.jpg'))
        self.opis.setIconSize(QSize(331, 241))
        self.opis.setIcon(QIcon('zombies/opisanie/opis7.jpg'))

    def vos(self):
        self.foto.setIconSize(QSize(250, 300))
        self.foto.setIcon(QIcon('zombies/zom8.jpg'))
        self.opis.setIconSize(QSize(331, 241))
        self.opis.setIcon(QIcon('zombies/opisanie/opis8.jpg'))

    def navihod(self):
        pass


if __name__ == '__main__':
    app = QApplication([])
    window = MyWidget()
    window.show()
    app.exec_()
