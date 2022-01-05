from PyQt5.QtWidgets import QApplication, QFrame, QPushButton, QRadioButton, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QButtonGroup, QGroupBox
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
        self.setStyleSheet('background-color:yellow')
        
        hbox = QHBoxLayout()
        
        btn = QPushButton("click me")
        btn.setStyleSheet('color:white')
        btn.setStyleSheet('background-color:green')
        
        
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet("background-color:red")
        frame.setLineWidth(0.6)
        hbox.addWidget(frame)
        
        hbox.addWidget(btn)
        
        
        self.setLayout(hbox)
        self.show()
        
    
if __name__=="__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
    

        
   