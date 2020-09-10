import JIO_FI_Status as JIO_Status
import time
import threading

#Autor : Saket Vats

batteryQuantity = 'lDashBatteryQuantity';
chargeStatus = 'lDashChargeStatus';
upLoadCurrentDataRate = 'lulCurrentDataRate';
downloadCurrentDataRate = 'ldlCurrentDataRate';
jio_req = JIO_Status.Jio_DataInfo()

def GetLatestStatus(ex):
    allData = []
    siteStatus = jio_req.sendRequest()
    if siteStatus:
        validIds = [batteryQuantity, chargeStatus, upLoadCurrentDataRate, downloadCurrentDataRate]
        if jio_req.ifResponseOk():
            allData = jio_req.getSelectedData(validIds)
            ex.updateStatus(batStatus = allData[chargeStatus], batper = allData[batteryQuantity],
            dlSpd = allData[downloadCurrentDataRate], ulSpd = allData[upLoadCurrentDataRate] )

def printit():
    threading.Timer(10.0, printit).start()
    GetLatestStatus(ex)

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'JioFi Status'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 200
        self.initUI()

    
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label1 = QLabel("Battery Status", self)
        self.label1.move(20,25)

        # Create textbox
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(150, 20)

        self.label2 = QLabel("Battery %", self)
        self.label2.move(20,55)

        # Create textbox
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(150, 50)

        self.label3 = QLabel("UL. Speed", self)
        self.label3.move(20,85)

        # Create textbox
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(150, 80)

        self.label4 = QLabel("DL. Speed", self)
        self.label4.move(20,115)

        # Create textbox
        self.textbox4 = QLineEdit(self)
        self.textbox4.move(150, 110)

        #self.textbox.resize(280,40)
        
        # Create a button in the window
        #self.button = QPushButton('Show text', self)
        #self.button.move(20,80)
        
        # connect button to function on_click
        #self.button.clicked.connect(self.on_click)
        
        self.show()
    
    def updateStatus(self, batStatus, batper, ulSpd, dlSpd):
        self.textbox1.setText(batStatus)
        self.textbox2.setText(batper)
        self.textbox3.setText(ulSpd)
        self.textbox4.setText(dlSpd)
    

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    #ex.updateStatus(batStatus = allData[chargeStatus], batper = allData[batteryQuantity],
    #dlSpd = allData[upLoadCurrentDataRate], ulSpd = allData[downloadCurrentDataRate] )
    #GetLatestStatus(ex)
    printit()
    sys.exit(app.exec_())
    




  #print "Hello, World!"

