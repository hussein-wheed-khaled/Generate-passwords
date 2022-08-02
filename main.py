import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
import random
import pyperclip


class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("enter111.ui",self)
        self.pushButton.clicked.connect(self.check)
        self.pushButton_2.clicked.connect(self.createe)
    def check(self):
        if len(self.lineEdit.text())<5:
            msg=QMessageBox()
            msg.setWindowTitle("PasswordGEN")
            msg.setFixedWidth(20)
            msg.setFixedHeight(20)
            msg.setText("your password is not strong try to create a new  ")
            msg.show()
            x = msg.exec_()
        else :
            msg = QMessageBox()
            msg.setWindowTitle("PasswordGEN")
            msg.setFixedWidth(20)
            msg.setFixedHeight(20)
            msg.setText("your password is strong ")
            msg.show()
            x = msg.exec_()

    def createe(self):
        newwindow = MainWindow2()
        widget.addWidget(newwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class MainWindow2(QDialog):

    def __init__(self):
     super(MainWindow2, self).__init__()
     loadUi("gen.ui", self)
     self.pushButton.clicked.connect(self.gen)
     self.lineEdit_2.setEnabled(False)
     self.pushButton_2.clicked.connect(self.copy)
    def gen(self):
        global password

        name=self.lineEdit.text()
        ch = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "!", "@", "#", "$"]
        r1=str(random.choice(name))
        r1.upper()


        r2 = random.choice(name)
        r3 = random.choice(name)
        r4 = random.choice(name)
        ch1 =random.choice(ch)
        ch2 = random.choice(ch)
        ch3 = random.choice(ch)
        ch4 = random.choice(ch)
        password = str(r1) + str(r2) + str(r3) + str(ch1) + str(ch2) + str(r4) + str(ch3) + str(ch4)
        self.lineEdit_2.setText(password)
    def copy(self):
        pyperclip.copy(password)



app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(495)
widget.setFixedHeight(342)
widget.show()
app.exec_()