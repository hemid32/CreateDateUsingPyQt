#-*- coding: UTF-8 -*-

from PyQt4 import uic
import sqlite3

qtCreatorFile = "untitled.ui"  # Enter file here.

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
        self.databes()
        self.crct1 = False
        self.crct2 = False
        self.crct3 = False
        self.img1_var = ' '
        self.img2_var = ' '
        self.img3_var = ' '






    def validati_form_chois(self):
        if (self.choi11.toPlainText() == '') :
            return  False
        elif (self.choi12.toPlainText() == ''):
            return False
        elif (self.choi13.toPlainText() == ''):
            return False
        elif (self.choi14.toPlainText() == ''):
            return False
        elif (self.choi21.toPlainText() == ''):
            return False
        elif (self.choi22.toPlainText() == ''):
            return False
        elif (self.choi23.toPlainText() == ''):
            return False
        elif (self.choi24.toPlainText() == ''):
            return False
        elif (self.choi31.toPlainText() == ''):
            return False
        elif (self.choi32.toPlainText() == ''):
            return False
        elif (self.choi33.toPlainText() == ''):
            return False
        elif (self.choi34.toPlainText() == ''):
            return False
        else:
            return  True

    def choi_correct(self):
        if(self.checkBox.isChecked()) :
            self.crct1 = self.choi11.toPlainText()
        if (self.checkBox_2.isChecked()):
            self.crct1 = self.choi12.toPlainText()
        if (self.checkBox_3.isChecked()):
            self.crct1 = self.choi13.toPlainText()
        if (self.checkBox_4.isChecked()):
            self.crct1 = self.choi14.toPlainText()
        if (self.checkBox_5.isChecked()):
            self.crct2 = self.choi21.toPlainText()
        if (self.checkBox_6.isChecked()):
            self.crct2 = self.choi22.toPlainText()
        if (self.checkBox_7.isChecked()):
            self.crct2 = self.choi23.toPlainText()
        if (self.checkBox_8.isChecked()):
            self.crct2 = self.choi24.toPlainText()
        if (self.checkBox_9.isChecked()):
            self.crct3 = self.choi31.toPlainText()
        if (self.checkBox_10.isChecked()):
            self.crct3 = self.choi32.toPlainText()
        if (self.checkBox_11.isChecked()):
            self.crct3 = self.choi33.toPlainText()
        if (self.checkBox_12.isChecked()):
            self.crct3 = self.choi34.toPlainText()
        if (self.crct1 != False and self.crct2 != False and self.crct3 != False) :
            return  True
        else :
            return  False

    def databes(self):
        #self.dbe = mysql.connector.connect(host='localhost' , user='root', password='12345' ,db='mydb')
        #self.cur = self.dbe.cursor()

        ######
        file = ('info2.db')
        self.conn = sqlite3.connect(file)
        self.cur =  self.conn.cursor()

        sql = ''' SELECT * FROM parti2 '''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for e in  data :
            print(e)

    def add_Date(self):

        #####################################add 2019 ##################"
        file = ('info2.db')
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()

        self.cur.execute('''INSERT INTO  parti2(title , qst, point 
        ,def11,def12,def13,def14,def15 , eq11,eq12,
        eq13,eq14, eq15 , choi11,choi12,choi13,choi14,
         crct1 ,def21,def22,def23,def24,eq21,eq22,eq23 , eq24,
         choi21,choi22,choi23,choi24,crct2,
                                          def31,def32,def33,def34,eq31,eq32,
                                          eq33,eq34,choi31,choi32,choi33,choi34,crct3 , img1 , img2 , img3)
                                          VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'
                                          ,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
                                          '%s','%s','%s','%s','%s','%s','%s',
                                          '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s' )''' % (
            self.titre.toPlainText() ,  'qst' , 'point' ,
            self.def11.toPlainText() , self.def12.toPlainText() ,self.def13.toPlainText() , self.def14.toPlainText() ,'def15',
            self.eq11.toPlainText(), self.eq12.toPlainText(), self.eq13.toPlainText(), self.eq14.toPlainText(), 'eq15' ,

            self.choi11.toPlainText() ,  self.choi12.toPlainText() ,  self.choi13.toPlainText() ,
            self.choi14.toPlainText(),self.crct1 ,
            self.def21.toPlainText(), self.def22.toPlainText(), self.def23.toPlainText(), self.def24.toPlainText(),
            self.eq21.toPlainText(), self.eq22.toPlainText(), self.eq23.toPlainText(),
            self.eq24.toPlainText(),

            self.choi21.toPlainText(), self.choi22.toPlainText(), self.choi23.toPlainText(),
            self.choi24.toPlainText(), self.crct2,
            self.def31.toPlainText(), self.def32.toPlainText(), self.def33.toPlainText(), self.def34.toPlainText(),
            self.eq31.toPlainText(), self.eq32.toPlainText(), self.eq33.toPlainText(),
            self.eq34.toPlainText(),

            self.choi31.toPlainText(), self.choi32.toPlainText(), self.choi33.toPlainText(),
            self.choi34.toPlainText(), self.crct3 , self.img1_var , self.img2_var , self.img3_var


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
        if(self.validati_form_chois()) :
            if (self.choi_correct()) :
                self.add_Date()
                print('crct1 = ' , self.crct1)
                print('crct2 = ' , self.crct2)
                print('crct3 = ' , self.crct3)
        else :
            self.Dilog_erurr()




    def Dilog_erurr(self):
        Qt.QMessageBox.information(self, u'نسييت واحد فارغ', u'نسيت فراغ')
        #pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
