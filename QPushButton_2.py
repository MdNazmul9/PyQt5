from PyQt5.QtWidgets import QApplication, QPushButton ,QMainWindow
import sys
from PyQt5 import QtCore, QtGui

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        title = "PyQt5 Push Button"
        left = 500
        top = 200
        width = 300
        height = 250
        iconName = "assets/home.png"
        
        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, top, width, height )
        self.show()
        

if __name__=="__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
