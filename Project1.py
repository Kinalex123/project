from PyQT5 import QtCore, QtGui, QtWidgets, uic

class MyWindow(QtWidgets, QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('Project1.ui', self)
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.arvg)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())