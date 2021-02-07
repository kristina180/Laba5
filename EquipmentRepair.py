
from PyQt5 import QtCore, QtGui, QtWidgets
from EquipmentRepair_show import  ShowEquipmentRepair
import MySQLdb   as mysql
from datetime import date

class EquipmentRepair(object):
    def show_EquipmentRepair(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =  Showus()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 262)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 50, 100, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 50, 100, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 20, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 20, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 130, 161, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.show_EquipmentRepair)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 80, 381, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.change)
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.add)
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.dels)
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 21))
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
        self.label.setText(_translate("MainWindow", "Repair"))
        self.label_2.setText(_translate("MainWindow", "DateRepair"))
        
        self.pushButton_4.setText(_translate("MainWindow", "Show_Repair"))
        self.pushButton.setText(_translate("MainWindow", "Change_Repair"))
        self.pushButton_2.setText(_translate("MainWindow", "Add_Repair"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete_Repair"))

    def change(self):

        try:
             EquipmentRepair_Repair= self.lineEdit.text()
             EquipmentRepair_DateRepair= self.lineEdit_2.text()
        
        except:
            return

        try:
            db = mysql.connect(host="localhost", user="root", passwd="1234", db="lab4")
            cur = db.cursor()
            ch1="""UPDATE EquipmentRepair SET EquipmentRepair_DateRepai = %s WHERE EquipmentRepair_Repair = %s"""
            ch2=(EquipmentRepair_DateRepair, EquipmentRepair_Repair, )
            cur.execute(ch1, ch2)
            db.commit()
            cur.close()
        finally:
            db.close()

    def add(self):

        try:
            EquipmentRepair_Repair= self.lineEdit.text()
            EquipmentRepair_DateRepair= self.lineEdit_2.text()            
           
        except:
            return
        db = mysql.connect(host="localhost", user="root", passwd="1234", db="lab4")
        cur = db.cursor()
        cur.execute('insert into user values(%s, %s)', \
                    ( EquipmentRepair_Repair, date.fromisoformat(EquipmentRepair_DateRepair) ,))
        db.commit()
        cur.close()
        db.close()

    def dels(self):


        db = mysql.connect(host="localhost", user="root", passwd="1234", db="lab4")
        cur = db.cursor()
        try:
            ids = int(self.lineEdit.text())
        except:
            return
        cur.execute("DELETE FROM EquipmentRepair WHERE EquipmentRepair_Repair = %s",(EquipmentRepair_Repair ,))
        db.commit()
        cur.close()
        db.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = EquipmentRepair()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
