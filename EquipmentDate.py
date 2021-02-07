from PyQt5 import QtCore, QtGui, QtWidgets
from EquipmentDate_show import  ShowEquipmentDate
import MySQLdb   as mysql
from datetime import date

class EquipmentDate(object):
    def show_EquipmentDate(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =  Showus()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 262)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 100, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 50, 100, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")       
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 50, 100, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")       
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(350, 50, 100, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")   
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(460, 50, 100, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")       
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(570, 50, 100, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")         
       
       
       
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 30, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 30, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 30, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(470, 30, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(580, 30, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")        
       
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 130, 161, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.show_EquipmentDate)
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
        self.label.setText(_translate("MainWindow", "EquipmentName"))
        self.label_2.setText(_translate("MainWindow", "EquipmentType"))
        self.label_3.setText(_translate("MainWindow", "StartWorkDate"))
        self.label_4.setText(_translate("MainWindow", "OperationalLife"))
        self.label_5.setText(_translate("MainWindow", "WhiteOffDate"))
        self.label_6.setText(_translate("MainWindow", "Repair"))        
        
        self.pushButton_4.setText(_translate("MainWindow", "Show_EquipmentDate"))
        self.pushButton.setText(_translate("MainWindow", "Change_EquipmentDate"))
        self.pushButton_2.setText(_translate("MainWindow", "Add_EquipmentDate"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete_EquipmentDate"))

    def change(self):

        try:
            EquipmentDate_EquipmentName = self.lineEdit_1.text(self.lineEdit.text())
            EquipmentDate_EquipmentType = self.lineEdit_2.text()
            EquipmentDate_StartWorkDate = self.lineEdit_3.text()
            EquipmentDate_OperationalLife = int(self.lineEdit_4.text())
            EquipmentDate_WhiteOffDate = self.lineEdit_5.text()
            EquipmentRepairs_Repair = self.lineEdit_6.text()            
           
        except:
            return

        try:
            db = mysql.connect(host="localhost", user="root", passwd="0000", db="db1")
            cur = db.cursor()
            ch1="""UPDATE EquipmentDate SET EquipmentDate_EquipmentType = %s, EquipmentDate_StartWorkDate = %s, EquipmentDate_OperationalLife = %s, EquipmentDate_WhiteOffDate = %s, EquipmentRepairs_Repair = %s  WHERE EquipmentDate_EquipmentName = %s"""
            ch2=(EquipmentDate_EquipmentName, EquipmentDate_EquipmentType, date.fromisoformat(EquipmentDate_StartWorkDate), int(EquipmentDate_OperationalLife), date.fromisoformat(EquipmentDate_WhiteOffDate), EquipmentRepairs_Repair)
            cur.execute(ch1, ch2)
            db.commit()
            cur.close()
        finally:
            db.close()

    def add(self):

        try:
            EquipmentDate_EquipmentName = self.lineEdit_1.text(self.lineEdit.text())
            EquipmentDate_EquipmentType = self.lineEdit_2.text()
            EquipmentDate_StartWorkDate = self.lineEdit_3.text()
            EquipmentDate_OperationalLife = int(self.lineEdit_4.text())
            EquipmentDate_WhiteOffDate = self.lineEdit_5.text()
            EquipmentRepair_Repair = self.lineEdit_6.text()            
        
        except:
            return
        db = mysql.connect(host="localhost", user="root", passwd="0000", db="db1")
        cur = db.cursor()
        cur.execute('insert into user values(%s, %s, %s, %s, %s, %s)', \
                    (EquipmentDate_EquipmentName, EquipmentDate_EquipmentType, date.fromisoformat(EquipmentDate_StartWorkDate), int(EquipmentDate_OperationalLife), date.fromisoformat(EquipmentDate_WhiteOffDate), EquipmentRepairs_Repair,))
        db.commit()
        cur.close()
        db.close()

    def dels(self):


        db = mysql.connect(host="localhost", user="root", passwd="0000", db="db1")
        cur = db.cursor()
        try:
            ids = int(self.lineEdit.text())
        except:
            return
        cur.execute("DELETE FROM EquipmentDate WHERE EquipmentDate_EquipmentName = %s",(int(ids),))
        db.commit()
        cur.close()
        db.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = EquipmentDate()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
