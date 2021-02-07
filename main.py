from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from user import User
from EquipmentRepair import EquipmentRepair
from EquipmentDate import EquipmentDate
from Invoice import Invoice
from ProductionSiteData import ProductionSiteData
from DataBackup import DataBackup
from ComponentParts import ComponentParts
from Warehouse import Warehouse
class Ui_MainWindow(object):
    def User(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = User()
        self.ui.setupUi(self.window)
        self.window.show()
    def EquipmentRepair(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = EquipmentRepair()
        self.ui.setupUi(self.window)
        self.window.show()
    def EquipmentDate(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = EquipmentDate()
        self.ui.setupUi(self.window)
        self.window.show()
    def Invoice(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Invoice()
        self.ui.setupUi(self.window)
        self.window.show()
    def ProductionSiteData(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ProductionSiteData()
        self.ui.setupUi(self.window)
        self.window.show()
    def DataBackup(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = DataBackup()
        self.ui.setupUi(self.window)
        self.window.show()
    def Warehouse(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Warehouse()
        self.ui.setupUi(self.window)
        self.window.show()
    def DataBackup(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = DataBackup()
        self.ui.setupUi(self.window)
        self.window.show()  
    def ComponentParts(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ComponentParts()
        self.ui.setupUi(self.window)
        self.window.show()  
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(228, 444)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 370, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.closeEvent)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 61, 21))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 40, 131, 301))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.User)
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.EquipmentRepair)
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.Invoice)
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.EquipmentDate)
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.ProductionSiteData)
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.DataBackup)
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.ComponentParts)
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.Warehouse)
        self.verticalLayout.addWidget(self.pushButton_9)        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 228, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "Chose:"))
        self.pushButton_2.setText(_translate("MainWindow", "User"))
        self.pushButton_3.setText(_translate("MainWindow", "EquipmentRepair"))
        self.pushButton_4.setText(_translate("MainWindow", "Invoice"))
        self.pushButton_5.setText(_translate("MainWindow", "EquipmentDate"))
        self.pushButton_6.setText(_translate("MainWindow", "ProductionSiteData"))
        self.pushButton_7.setText(_translate("MainWindow", "DateBackup"))
        self.pushButton_8.setText(_translate("MainWindow", "ComponentParts"))
        self.pushButton_9.setText(_translate("MainWindow", "Warehouse"))

    def closeEvent(self, event):
            self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
