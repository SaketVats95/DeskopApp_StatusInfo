import JIO_FI_Status as JIO_Status

import time



jio_req = JIO_Status.Jio_DataInfo()
jio_req.sendRequest()
validIds = ['lDashBatteryQuantity', 'lDashChargeStatus', 'lulCurrentDataRate', 'ldlCurrentDataRate']
if jio_req.ifResponseOk():
    print(jio_req.getSelectedData(validIds))

from PyQt5 import QtWidgets, QtGui, QtCore
class PyQtApp(QtWidgets.QWidget):
   
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("PyQt Application")
        self.setWindowIcon(QtGui.QIcon("Your/image/file.png"))
        self.setMinimumWidth(resolution.width() / 3)
        self.setMinimumHeight(resolution.height() / 1.5)
        self.setStyleSheet('''QWidget {background-color:
                           rgba(0,41,59,255);}
                           QScrollBar:horizontal {
                           width: 1px; height: 1px;
                           background-color: rgba(0,41,59,255);}  
                           QScrollBar:vertical {width: 1px;
                           height: 1px;
                           background-color: rgba(0,41,59,255);}''')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    desktop = QtWidgets.QApplication.desktop()
    resolution = desktop.availableGeometry()
    myapp = PyQtApp()
    myapp.setWindowOpacity(0.95)
    myapp.show()
    myapp.move(resolution.center() - myapp.rect().center())
    sys.exit(app.exec_())
else:
    desktop = QtWidgets.QApplication.desktop()
    resolution = desktop.availableGeometry()