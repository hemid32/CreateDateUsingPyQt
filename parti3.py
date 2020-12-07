#-*- coding: UTF-8 -*-
from PyQt5 import uic
import sqlite3

qtCreatorFile = "untitledparti3.ui"  # Enter file here.



import sys
from PyQt5 import QtCore, QtGui, uic , Qt , QtWidgets
from PyQt5.QtGui import * #QApplication, QCompleter, QLineEdit, QStringListModel
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

    def Recouver_Latex(self, text):
        if (text == ''):
            return text
        else:
            if ('**' in text) :
                t = text.replace('**' , '')
                h = '\\text' + '{'  + t + '}'
            else :
                h = text
            text = '$$' + h + '$$'
            return text


    def add_Date(self):
        #####################################add 2019 ##################"
        file = ('info2.db')
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()
        self.cur.execute('''INSERT INTO  parti3(title  ,point , methode 
        ,def11,def12,def13,def14,def15 , eq11,eq12,
        eq13,eq14, eq15 , img  , qst1 , aid1 , crr1 ,  qst2 , aid2 , crr2, qst3 , aid3 , crr3 , qst4 , aid4 , crr4 
        , qst5 , aid5 , crr5)
                                          VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'
                                          ,'%s','%s','%s','%s','%s','%s' ,'%s','%s','%s','%s','%s','%s'
                                           ,'%s','%s','%s','%s','%s','%s','%s')''' % (
            self.titre.toPlainText() , ' ' , ' ',
            self.def11.toPlainText() , self.def12.toPlainText() ,self.def13.toPlainText() , self.def14.toPlainText() ,self.def15.toPlainText(),
            self.Recouver_Latex(self.eq11.toPlainText()), self.Recouver_Latex(self.eq12.toPlainText()), self.Recouver_Latex(self.eq13.toPlainText()), self.Recouver_Latex(self.eq14.toPlainText()),
            self.Recouver_Latex(self.eq15.toPlainText()) , self.img1_var  , self.qst1.toPlainText() ,self.Recouver_Latex(self.aid1.toPlainText()) , self.crr1.toPlainText()
            , self.qst2.toPlainText(), self.Recouver_Latex(self.aid2.toPlainText()), self.crr2.toPlainText()
            , self.qst3.toPlainText(), self.Recouver_Latex(self.aid3.toPlainText()), self.crr3.toPlainText()
            , self.qst4.toPlainText(), self.Recouver_Latex(self.aid4.toPlainText()), self.crr4.toPlainText()
            , self.qst5.toPlainText(), self.Recouver_Latex(self.aid5.toPlainText()), self.crr5.toPlainText()
        )
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
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
