# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 490)
        MainWindow.setMinimumSize(QtCore.QSize(361, 490))
        MainWindow.setMaximumSize(QtCore.QSize(361, 490))
        self.CentralWidget = QtWidgets.QWidget(MainWindow)
        self.CentralWidget.setObjectName("CentralWidget")
        self.MainFrame = QtWidgets.QFrame(self.CentralWidget)
        self.MainFrame.setGeometry(QtCore.QRect(0, 0, 361, 501))
        self.MainFrame.setStyleSheet("background-color: rgb(64, 64, 83);\n"
"")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.HeaderFrame = QtWidgets.QFrame(self.MainFrame)
        self.HeaderFrame.setGeometry(QtCore.QRect(0, 0, 371, 61))
        self.HeaderFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HeaderFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.HeaderFrame.setObjectName("HeaderFrame")
        self.HeadingLabel = QtWidgets.QLabel(self.HeaderFrame)
        self.HeadingLabel.setGeometry(QtCore.QRect(80, 10, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(22)
        font.setUnderline(False)
        self.HeadingLabel.setFont(font)
        self.HeadingLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.HeadingLabel.setObjectName("HeadingLabel")
        self.ScoreMessageFrame = QtWidgets.QFrame(self.MainFrame)
        self.ScoreMessageFrame.setGeometry(QtCore.QRect(0, 70, 371, 61))
        self.ScoreMessageFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ScoreMessageFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ScoreMessageFrame.setObjectName("ScoreMessageFrame")
        self.XScoreFrame = QtWidgets.QFrame(self.ScoreMessageFrame)
        self.XScoreFrame.setGeometry(QtCore.QRect(0, 0, 181, 31))
        self.XScoreFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.XScoreFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.XScoreFrame.setObjectName("XScoreFrame")
        self.XScoreLabel = QtWidgets.QLabel(self.XScoreFrame)
        self.XScoreLabel.setGeometry(QtCore.QRect(130, 0, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.XScoreLabel.setFont(font)
        self.XScoreLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.XScoreLabel.setObjectName("XScoreLabel")
        self.XLabel = QtWidgets.QLabel(self.XScoreFrame)
        self.XLabel.setGeometry(QtCore.QRect(20, 5, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.XLabel.setFont(font)
        self.XLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.XLabel.setObjectName("XLabel")
        self.OScoreFrame = QtWidgets.QFrame(self.ScoreMessageFrame)
        self.OScoreFrame.setGeometry(QtCore.QRect(190, 0, 181, 31))
        self.OScoreFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.OScoreFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.OScoreFrame.setObjectName("OScoreFrame")
        self.OLabel = QtWidgets.QLabel(self.OScoreFrame)
        self.OLabel.setGeometry(QtCore.QRect(10, 5, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.OLabel.setFont(font)
        self.OLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.OLabel.setObjectName("OLabel")
        self.OScoreLabel = QtWidgets.QLabel(self.OScoreFrame)
        self.OScoreLabel.setGeometry(QtCore.QRect(120, 0, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.OScoreLabel.setFont(font)
        self.OScoreLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.OScoreLabel.setObjectName("OScoreLabel")
        self.MessageFrame = QtWidgets.QFrame(self.ScoreMessageFrame)
        self.MessageFrame.setGeometry(QtCore.QRect(100, 30, 181, 31))
        self.MessageFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MessageFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MessageFrame.setObjectName("MessageFrame")
        self.MessageLabel = QtWidgets.QLabel(self.MessageFrame)
        self.MessageLabel.setGeometry(QtCore.QRect(40, 0, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.MessageLabel.setFont(font)
        self.MessageLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.MessageLabel.setObjectName("MessageLabel")
        self.BoardFrame = QtWidgets.QFrame(self.MainFrame)
        self.BoardFrame.setGeometry(QtCore.QRect(60, 150, 231, 231))
        self.BoardFrame.setStyleSheet("background-color: rgb(152, 152, 152);")
        self.BoardFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BoardFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BoardFrame.setObjectName("BoardFrame")
        self.Button_6 = QtWidgets.QPushButton(self.BoardFrame)
        self.Button_6.setGeometry(QtCore.QRect(0, 160, 77, 77))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Button_6.setFont(font)
        self.Button_6.setStyleSheet("background-color: rgb(64, 64, 83);\n"
"color: rgb(255, 255, 255);")
        self.Button_6.setObjectName("Button_6")
        self.Button_7 = QtWidgets.QPushButton(self.BoardFrame)
        self.Button_7.setGeometry(QtCore.QRect(80, 160, 77, 77))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Button_7.setFont(font)
        self.Button_7.setStyleSheet("background-color: rgb(64, 64, 83);\n"
"color: rgb(255, 255, 255);")
        self.Button_7.setObjectName("Button_7")
        self.Button_8 = QtWidgets.QPushButton(self.BoardFrame)
        self.Button_8.setGeometry(QtCore.QRect(160, 160, 77, 77))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Button_8.setFont(font)
        self.Button_8.setStyleSheet("background-color: rgb(64, 64, 83);\n"
"color: rgb(255, 255, 255);")
        self.Button_8.setObjectName("Button_8")
        self.Button_5 = QtWidgets.QPushButton(self.BoardFrame)
        self.Button_5.setGeometry(QtCore.QRect(160, 80, 77, 77))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Button_5.setFont(font)
        self.Button_5.setStyleSheet("background-color: rgb(64, 64, 83);\n"
"color: rgb(255, 255, 255);")
        self.Button_5.setObjectName("Button_5")
        self.Button_4 = QtWidgets.QPushButton(self.BoardFrame)
        self.Button_4.setGeometry(QtCore.QRect(80, 80, 77, 77))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Button_4.setFont(font)
        self.Button_4.setStyleSheet("background-color: rgb(64, 64, 83);\n"
"color: rgb(255, 255, 255);")
        self.Button_4.setObjectName("Button_4")
        self.Button_3 = QtWidgets.QPushButton(self.BoardFrame)
        self.Button_3.setGeometry(QtCore.QRect(0, 80, 77, 77))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Button_3.setFont(font)
        self.Button_3.setStyleSheet("background-color: rgb(64, 64, 83);\n"
"color: rgb(255, 255, 255);")
        self.Button_3.setObjectName("Button_3")
        self.Button_2 = QtWidgets.QPushButton(self.BoardFrame)
        self.Button_2.setGeometry(QtCore.QRect(160, 0, 77, 77))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Button_2.setFont(font)
        self.Button_2.setStyleSheet("background-color: rgb(64, 64, 83);\n"
"color: rgb(255, 255, 255);")
        self.Button_2.setObjectName("Button_2")
        self.Button_1 = QtWidgets.QPushButton(self.BoardFrame)
        self.Button_1.setGeometry(QtCore.QRect(80, 0, 77, 77))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Button_1.setFont(font)
        self.Button_1.setStyleSheet("background-color: rgb(64, 64, 83);\n"
"color: rgb(255, 255, 255);")
        self.Button_1.setObjectName("Button_1")
        self.Button_0 = QtWidgets.QPushButton(self.BoardFrame)
        self.Button_0.setGeometry(QtCore.QRect(0, 0, 77, 77))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Button_0.setFont(font)
        self.Button_0.setStyleSheet("background-color: rgb(64, 64, 83);\n"
"color: rgb(255, 255, 255);")
        self.Button_0.setObjectName("Button_0")
        self.Restart_Button = QtWidgets.QPushButton(self.MainFrame)
        self.Restart_Button.setGeometry(QtCore.QRect(110, 400, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.Restart_Button.setFont(font)
        self.Restart_Button.setStyleSheet("background-color: rgb(255, 224, 98);")
        self.Restart_Button.setObjectName("Restart_Button")
        MainWindow.setCentralWidget(self.CentralWidget)
        self.ActionNew_Game = QtWidgets.QAction(MainWindow)
        self.ActionNew_Game.setObjectName("ActionNew_Game")
        self.ActionExit = QtWidgets.QAction(MainWindow)
        self.ActionExit.setObjectName("ActionExit")
        self.ActionUndo = QtWidgets.QAction(MainWindow)
        self.ActionUndo.setObjectName("ActionUndo")
        self.ActionRedo = QtWidgets.QAction(MainWindow)
        self.ActionRedo.setObjectName("ActionRedo")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.HeadingLabel.setText(_translate("MainWindow", "Tic Tac Toe"))
        self.XScoreLabel.setText(_translate("MainWindow", "-"))
        self.XLabel.setText(_translate("MainWindow", "X"))
        self.OLabel.setText(_translate("MainWindow", "O"))
        self.OScoreLabel.setText(_translate("MainWindow", "-"))
        self.MessageLabel.setText(_translate("MainWindow", "X\'s Turn"))
        self.Button_6.setText(_translate("MainWindow", "-"))
        self.Button_7.setText(_translate("MainWindow", "-"))
        self.Button_8.setText(_translate("MainWindow", "-"))
        self.Button_5.setText(_translate("MainWindow", "-"))
        self.Button_4.setText(_translate("MainWindow", "-"))
        self.Button_3.setText(_translate("MainWindow", "-"))
        self.Button_2.setText(_translate("MainWindow", "-"))
        self.Button_1.setText(_translate("MainWindow", "-"))
        self.Button_0.setText(_translate("MainWindow", "-"))
        self.Restart_Button.setText(_translate("MainWindow", "Restart"))
        self.ActionNew_Game.setText(_translate("MainWindow", "New Game"))
        self.ActionExit.setText(_translate("MainWindow", "Exit"))
        self.ActionUndo.setText(_translate("MainWindow", "Undo"))
        self.ActionRedo.setText(_translate("MainWindow", "Redo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
