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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myapp = PyQtApp()
    myapp.show()
    sys.exit(app.exec_())