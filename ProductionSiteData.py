from PyQt5 import QtCore, QtGui, QtWidgets
from ProductionSiteData_show import  ShowProductionSiteData
import MySQLdb   as mysql
from datetime import date

class ProductionSiteData(object):
    def show_ProductionSiteData(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =  ShowDateBackup()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 262)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 50, 100, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 50, 100, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 50, 100, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")    
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 150, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(185, 20, 150, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 20, 150, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")        
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 130, 161, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.show_ProductionSiteData)
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
        self.label.setText(_translate("MainWindow", "NameProductionSite"))
        self.label_2.setText(_translate("MainWindow", "AdressProductionSite"))
        self.label_3.setText(_translate("MainWindow", "StartWorkProductionSite"))
        
        self.pushButton_4.setText(_translate("MainWindow", "Show_ProductionSite"))
        self.pushButton.setText(_translate("MainWindow", "Change_ProductionSite"))
        self.pushButton_2.setText(_translate("MainWindow", "Add_ProductionSite"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete_ProductionSite"))

    def change(self):

        try:
             ProductionSiteData_NameProductionSite= self.lineEdit.text()
             ProductionSiteData_AdressProductionSite= self.lineEdit_2.text()
             ProductionSiteData_StartWorkProductionSite= self.lineEdit_3.text()
        
        except:
            return

        try:
            db = mysql.connect(host="localhost", user="root", passwd="0000", db="db1")
            cur = db.cursor()
            ch1="""UPDATE ProductionSiteData SET ProductionSiteData_AdressProductionSite= %s, ProductionSiteData_AdressProductionSite = %s WHERE  ProductionSite_NameProductionSite = %s"""
            ch2=( ProductionSiteData_AdressProductionSite, date.fromisoformat(ProductionSiteData_StartWorkProductionSite), ProductionSiteData_NameProductionSite, )
            cur.execute(ch1, ch2)
            db.commit()
            cur.close()
        finally:
            db.close()

    def add(self):

        try:
             ProductionSiteData_NameProductionSite= self.lineEdit.text()
             ProductionSiteData_AdressProductionSite= self.lineEdit_2.text()
             ProductionSiteData_StartWorkProductionSite= self.lineEdit_3.text()       
           
        except:
            return
        db = mysql.connect(host="localhost", user="root", passwd="0000", db="db1")
        cur = db.cursor()
        cur.execute('insert into ProductionSiteData values(%s, %s, %s)', \
                    ( ProductionSiteData_NameProductionSite, ProductionSiteData_AdressProductionSite, date.fromisoformat(ProductionSiteData_StartWorkProductionSite),))
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
        cur.execute("DELETE FROM ProductionSiteData WHERE ProductionSiteData_NameProductionSite",(ProductionSiteData_NameProductionSite ,))
        db.commit()
        cur.close()
        db.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ProductionSiteData()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
