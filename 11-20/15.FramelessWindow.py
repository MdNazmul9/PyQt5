from PyQt5.QtWidgets import QApplication, QPushButton, QRadioButton, QSizeGrip, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QButtonGroup, QGroupBox
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect

from PyQt5.QtGui import QPixmap
class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.title = "PyQt5 QButtonGroup" 
     
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "assets/home.png"
        
        self.InitWindow()
        
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        
        vbox = QVBoxLayout()
        sizegrip = QSizeGrip(self)
        vbox.addWidget(sizegrip)
        self.setLayout(vbox)
        
        
        self.show()
        
if __name__=="__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
    

        
   