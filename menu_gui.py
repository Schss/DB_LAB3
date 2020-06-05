# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from data_functions import create_data, delete_data
from database_created_gui import Ui_database_created
from new_data_name_gui import Ui_NameMainWindow
from delete_data_gui import Ui_DeleteWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(213, 221, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 30, 381, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(210, 180, 371, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.create_data = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.create_data.setStyleSheet("background-color: rgb(255, 250, 189);\n"
                                       "font: 18pt \"MS Shell Dlg 2\";")
        self.create_data.setObjectName("create_data")

        ##########################################################################################
        ##########################################################################################
        self.create_data.clicked.connect(self.open_create)


        ##########################################################################################
        ##########################################################################################
        self.verticalLayout.addWidget(self.create_data)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 250, 189);\n"
                                        "font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        #######################################################################################

        self.pushButton3.clicked.connect(self.watch_button)

        #####################################################################################
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 250, 189);\n"
                                        "font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setStyleSheet("background-color: rgb(255, 250, 189);\n"
                                      "font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        ##################################################################
        self.pushButton.clicked.connect(self.delete_button)
        ################################################################
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 250, 189);\n"
                                        "font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def open_create(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_NameMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def delete_button(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DeleteWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def watch_button(self):



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Работа с базами данных\n"
                                                    " Продукты и продажи"))
        self.create_data.setText(_translate("MainWindow", "создать"))
        self.pushButton_3.setText(_translate("MainWindow", "посмотреть"))
        self.pushButton_4.setText(_translate("MainWindow", "поиск"))
        self.pushButton.setText(_translate("MainWindow", "удалить"))
        self.pushButton_2.setText(_translate("MainWindow", "подключиться к существующей"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())