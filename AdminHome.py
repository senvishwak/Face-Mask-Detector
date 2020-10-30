from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QGraphicsBlurEffect

from train_newmodel import build
from Prediction import Ui_Detection
import sys
import cv2
from mask_detection_video import mask_video


class Ui_AdminHome(object):


    def cnnbuild(self):
        try:
            build()
            self.showMessageBox("Message", "Trained Successfully.")

        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def detect(self):

        try:
            self.admn = QtWidgets.QDialog()
            self.ui = Ui_Detection()
            self.ui.setupUi(self.admn)
            self.admn.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def webCamera(self):
        try:
            mask_video()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 447)
        # Dialog.setStyleSheet("background-color: rgb(170, 85, 0);")
        self.image_label = QtWidgets.QLabel(Dialog)
        pixmap = QPixmap('corona.jpg')
        self.image_label.setPixmap(pixmap)
        self.image_label.resize(700, 447)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 0, 650, 71))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 28pt \"Georgia\";")  # \nimage: url(COVID19.png);
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 120, 241, 51))
        self.pushButton.setStyleSheet("background-color: rgb(51,153,255);\n"
                                      "font: 14pt \"Franklin Gothic\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.cnnbuild)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 220, 241, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(51,153,255);\n"
                                        "font: 14pt \"Franklin Gothic\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.detect)

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 320, 241, 51))
        self.pushButton_3.setStyleSheet("background-color: rgb(51,153,255);\n"
                                        "font: 14pt \"Franklin Gothic\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.webCamera)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Home"))
        Dialog.setWindowIcon(QIcon("logo.png"))
        self.label.setText(_translate("Dialog", "\nFace Mask Detector"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton.setText(_translate("Dialog", "Build New Model"))
        self.pushButton_2.setText(_translate("Dialog", "Image Detection"))
        self.pushButton_3.setText(_translate("Dialog", "Live Camera"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_AdminHome()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
