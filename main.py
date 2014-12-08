import sys

from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *

import ui_form

print "trying to import rpy2"
from rpy2 import robjects as ro

print("main started")

class HelloWorldDlg(QtGui.QDialog, ui_form.Ui_Dialog):
    def __init__(self, parent=None):
        super(HelloWorldDlg, self).__init__(parent)
        self.setupUi(self)
        
        self.result_lbl.setText("Results is %d" % ro.r("2+3")[0])
        
def start():
    app = QApplication(sys.argv)
    form = HelloWorldDlg()
    form.show()
    form.raise_()
    app.exec_()

if __name__ == '__main__':
    #pass        
    start()