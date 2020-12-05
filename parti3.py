#-*- coding: UTF-8 -*-

from PyQt4 import uic
import sqlite3

qtCreatorFile = "untitledparti3.ui"  # Enter file here.

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import sys
from PyQt4 import QtCore, QtGui, uic , Qt
from PyQt4.QtGui import QApplication, QCompleter, QLineEdit, QStringListModel
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self  ):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.var = 10
        self.setupUi(self)
        self.bottun()
        self.crct1 = False
        self.crct2 = False
        self.crct3 = False
        self.img1_var = ' '
        self.img2_var = ' '
        self.img3_var = ' '

    def Recouver_Latex(self, text):
        if (text == ''):
            return text
        else:
            text = '$$' + text + '$$'
            return text


    def add_Date(self):
        #####################################add 2019 ##################"
        file = ('info2.db')
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()
        self.cur.execute('''INSERT INTO  parti3(title , qst ,crr ,point , methode 
        ,def11,def12,def13,def14,def15 , eq11,eq12,
        eq13,eq14, eq15 , img)
                                          VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'
                                          ,'%s','%s','%s','%s','%s','%s' )''' % (
            self.titre.toPlainText() , ' ' , self.crr.toPlainText() , ' ' , ' ' ,
            self.def11.toPlainText() , self.def12.toPlainText() ,self.def13.toPlainText() , self.def14.toPlainText() ,self.def15.toPlainText(),
            self.eq11.toPlainText(), self.eq12.toPlainText(), self.eq13.toPlainText(), self.eq14.toPlainText(),
            self.eq15.toPlainText() , self.img1_var)
        )
        self.conn.commit()
        Qt.QMessageBox.information(self, u'صحيت', u'تم اضافة البيانات')

    def open_img_1(self):
        save__ =  Qt.QFileDialog.getOpenFileName(self,caption = 'select img' , directory = "/" , filter = 'AU filles(*.*)')
        name = save__.split('/')
        self.img1.setText(name[-1])
        self.img1_var = name[-1]
        #find = str(save__).find('/' , len(save__))
        #print(find)


    def bottun(self):
        self.pushButton.clicked.connect(self.Button_OK)
        self.imgBtn1.clicked.connect(self.open_img_1)


    def Button_OK(self):
        print('text')
        #self.validati_form_chois()
        self.add_Date()





    def Dilog_erurr(self):
        Qt.QMessageBox.information(self, u'نسييت واحد فارغ', u'نسيت فراغ')
        #pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
