#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
import os

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        #self.setToolTip('Login with your<b>LDAP</b> username and password')
        lbl1 = QtGui.QLabel('Username', self)
        lbl1.move(15, 30)

        lbl2 = QtGui.QLabel('Password', self)
        lbl2.move(15, 70)
       
        self.setGeometry(300, 300, 400, 150)
        self.setWindowTitle('Moodle File Downloader')
        self.setWindowIcon(QtGui.QIcon('moodleicon.png'))     
        
        
        btn = QtGui.QPushButton('Login', self)
        btn.resize(btn.sizeHint())
        btn.move(35, 120)
        
        qbtn = QtGui.QPushButton('Cancel', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(135, 120)
        
        self.show()
        
       
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    