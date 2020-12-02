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
        self.crct4 = False



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
            self.crct2 = self.choi31.toPlainText()
        if (self.checkBox_10.isChecked()):
            self.crct2 = self.choi32.toPlainText()
        if (self.checkBox_11.isChecked()):
            self.crct2 = self.choi33.toPlainText()
        if (self.checkBox_12.isChecked()):
            self.crct2 = self.choi34.toPlainText()

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
        file = ('data.db')
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()
        #############################################################"

        sql = ''' SELECT * FROM parti1 '''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        i = 0
        m = 0



        """
        self.cur.execute('''INSERT INTO 
                                          parti1(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,line21,line22,line23,line24,line25,line26,line27,line29,line30,line31,line32,line33,line34,line35,line36,line37,line38,line39,line40,line41,
                                          L7_0 , L7_1 , L7_2 , L7_3 , L7_4 , L7_5 ,L7_6  , L7_7 , L7_8 , L7_9 , L8_0 , L8_1 , L8_2 , L8_3 , L8_4 , L8_5 , L8_6 , L8_7 , L8_8 , L8_9)
                                          VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s' )''' % ())
        self.conn.commit()
        m = self.line30.text()
        self.comboBox.addItem(m)
        Qt.QMessageBox.information(self, u'صحيت', u'تم اضافة الدولة الي قاعدة البايانات بنجاح')
        """

    def bottun(self):
        self.pushButton.clicked.connect(self.prints)

    def prints(self):
        print('text')
        #self.validati_form_chois()
        self.choi_correct()



    def save_fille(self):

        Qt.QMessageBox.information(self, u'صحيت', u'تم')
        #pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
