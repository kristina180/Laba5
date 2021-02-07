from PyQt5 import QtCore, QtGui, QtWidgets
from user_show import  Showus
import MySQLdb   as mysql
from datetime import date

class User(object):
    def show_User(self):
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
        self.label_4.setGeometry(QtCore.QRect(350, 30, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
       
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 130, 161, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.show_User)
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
        self.label.setText(_translate("MainWindow", "UserName"))
        self.label_2.setText(_translate("MainWindow", "UserSumane"))
        self.label_3.setText(_translate("MainWindow", "UserLogin"))
        self.label_4.setText(_translate("MainWindow", "UserPassword"))
        
        self.pushButton_4.setText(_translate("MainWindow", "Show_Users"))
        self.pushButton.setText(_translate("MainWindow", "Change_User"))
        self.pushButton_2.setText(_translate("MainWindow", "Add_User"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete_User"))

    def change(self):

        try:
            user_Username = self.lineEdit_1.text(self.lineEdit.text())
            user_UserSuname = self.lineEdit_2.text()
            user_UserLogin = self.lineEdit_3.text()
            user_UserPassword = self.lineEdit_4.text()
            
        except:
            return

        try:
            db = mysql.connect(host="localhost", user="root", passwd="0000", db="db1")
            cur = db.cursor()
            ch1="""UPDATE user SET user_UserSumane = %s, user_UserLogin = %s, user_UserPassword = %s  WHERE user_Username = %s"""
            ch2=(user_Username, user_UserSuname, user_UserLogin, user_UserPassword)
            cur.execute(ch1, ch2)
            db.commit()
            cur.close()
        finally:
            db.close()

    def add(self):

        try:
            user_UserName = self.lineEdit_1.text()
            user_UserSuname = self.lineEdit_2.text()
            user_UserLogin = self.lineEdit_3.text()
            user_UserPassword = self.lineEdit_4.text()
        
        except:
            return
        db = mysql.connect(host="localhost", user="root", passwd="0000", db="db1")
        cur = db.cursor()
        cur.execute('insert into user values(%s, %s, %s, %s)', \
                    (user_UserName, user_UserSuname, user_UserLogin, user_UserPassword,))
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
        cur.execute("DELETE FROM user WHERE user_UserName = %s",(int(ids),))
        db.commit()
        cur.close()
        db.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = User()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
