from PyQt5.QtWidgets import QApplication, QFrame, QLineEdit, QSplitter, QPushButton, QRadioButton, QSplitter, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QButtonGroup, QGroupBox
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect, Qt, left

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
        
        hbox = QHBoxLayout()
        
        left = QFrame()
        left.setFrameShape(QFrame.StyledPanel)
        
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)
        spliter1 = QSplitter(Qt.Horizontal)
        lineedit = QLineEdit()
        lineedit.setStyleSheet('background-color:green')
        
        spliter1.addWidget(left)
        spliter1.addWidget(lineedit)
        spliter1.setSizes([200,200])
        spliter1.setStyleSheet('background-color:red')
        
        spliter2 = QSplitter(Qt.Vertical)
        spliter2.addWidget(spliter1)
        spliter2.addWidget(bottom)
        spliter2.setStyleSheet('background-color:yellow')
        
        hbox.addWidget(spliter2)
        self.setLayout(hbox)
        
        self.show()
        
    
if __name__=="__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
    

        
   