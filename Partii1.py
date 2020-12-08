#-*- coding: UTF-8 -*-

from PyQt5 import uic
import sqlite3

qtCreatorFile = "untitledparti1.ui"  # Enter file here.

import sys


import sys
from PyQt5 import QtCore, QtGui, uic , Qt , QtWidgets
from PyQt5.QtGui import * # QApplication, QCompleter, QLineEdit, QStringListModel
import sys

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self  ):
        QtWidgets.QMainWindow.__init__(self)
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
        self.databes()


    def databes(self):
        #self.dbe = mysql.connector.connect(host='localhost' , user='root', password='12345' ,db='mydb')
        #self.cur = self.dbe.cursor()

        ######
        file = ('info2.db')
        self.conn = sqlite3.connect(file)
        self.cur =  self.conn.cursor()

        sql = ''' SELECT * FROM parti1 '''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        print(len(data))
        self.lcdNumber.display(len(data))


    def NewLine(self, text):
        if ('#' in text):
            text.replace('#', '\\\\')

        return text

    def Recouver_Latex(self, text):
        if (text == ''):
            return text
        else:
            text = '$$' + text + '$$'
            return self.NewLine(text)


    def add_Date(self):
        #####################################add 2019 ##################"
        file = ('info2.db')
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()
        self.cur.execute('''INSERT INTO  parti1(title , titleP1
        ,def11,def12,def13,def14,def15 , eq11,eq12,
        eq13,eq14, eq15 , titleP2 , def21,def22,def23,def24,def25 ,  eq21,eq22,
        eq23,eq24, eq25 , titleP3 , def31,def32,def33,def34,def35, eq31,eq32,
        eq33,eq34, eq35  , img1 , img2 , img3)
                                          VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'
                                          ,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
                                          '%s','%s','%s','%s','%s','%s','%s',
                                          '%s','%s','%s','%s','%s','%s','%s')''' % (
            self.titre.toPlainText() ,self.titrep1.toPlainText() ,
            self.def11.toPlainText() , self.def12.toPlainText() ,self.def13.toPlainText() , self.def14.toPlainText() ,self.def15.toPlainText(),
            self.Recouver_Latex(self.eq11.toPlainText()), self.Recouver_Latex(self.eq12.toPlainText()), self.Recouver_Latex(self.eq13.toPlainText()), self.Recouver_Latex(self.eq14.toPlainText()), self.Recouver_Latex(self.eq15.toPlainText()) ,


            self.titrep2.toPlainText() , self.def21.toPlainText(), self.def22.toPlainText(), self.def23.toPlainText(), self.def24.toPlainText(),
            self.def25.toPlainText(),self.Recouver_Latex(self.eq21.toPlainText()), self.Recouver_Latex(self.eq22.toPlainText()), self.Recouver_Latex(self.eq23.toPlainText()),
            self.Recouver_Latex(self.eq24.toPlainText()),self.Recouver_Latex(self.eq25.toPlainText()),

            self.titrep3.toPlainText() ,
            self.def31.toPlainText(), self.def32.toPlainText(), self.def33.toPlainText(), self.def34.toPlainText(),self.def35.toPlainText(),
            self.Recouver_Latex(self.eq31.toPlainText()), self.Recouver_Latex(self.eq32.toPlainText()), self.Recouver_Latex(self.eq33.toPlainText()),
            self.Recouver_Latex(self.eq34.toPlainText()),  self.Recouver_Latex(self.eq35.toPlainText()), self.img1_var , self.img2_var , self.img3_var
        ))
        self.conn.commit()
        Qt.QMessageBox.information(self, u'صحيت', u'تم اضافة البيانات')

    def open_img_1(self):
        save__ =  Qt.QFileDialog.getOpenFileName(self,caption = 'select img' , directory = "/" , filter = 'AU filles(*.*)')
        name = save__.split('/')
        self.img1.setText(name[-1])
        self.img1_var = name[-1]
        #find = str(save__).find('/' , len(save__))
        #print(find)
    def open_img_2(self):
        save__ =  Qt.QFileDialog.getOpenFileName(self,caption = 'select img' , directory = "/" , filter = 'AU filles(*.*)')
        name = save__.split('/')
        self.img2.setText(name[-1])
        self.img2_var = name[-1]

        #find = str(save__).find('/' , len(save__))
        #print(find)
    def open_img_3(self):
        save__ =  Qt.QFileDialog.getOpenFileName(self,caption = 'select img' , directory = "/" , filter = 'AU filles(*.*)')
        name = save__.split('/')
        self.img3.setText(name[-1])
        self.img3_var = name[-1]

        #find = str(save__).find('/' , len(save__))
        #print(find)



    def bottun(self):
        self.pushButton.clicked.connect(self.Button_OK)
        self.imgBtn1.clicked.connect(self.open_img_1)
        self.imgBtn2.clicked.connect(self.open_img_2)
        self.imgBtn3.clicked.connect(self.open_img_3)

    def Button_OK(self):
        print('text')
        #self.validati_form_chois()
        self.add_Date()





    def Dilog_erurr(self):
        Qt.QMessageBox.information(self, u'نسييت واحد فارغ', u'نسيت فراغ')
        #pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
