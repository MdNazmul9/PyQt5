from PyQt5.QtWidgets import QApplication, QCheckBox, QDialog, QGroupBox, QHBoxLayout, QLabel, QVBoxLayout
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect

from PyQt5.QtGui import QPixmap
class Window(QDialog):
    def __init__(self):
        super().__init__()
        
        self.title = "PyQt5 checkbox" 
     
        self.left = 200
        self.top = 100
        self.width = 600
        self.height = 300
        self.iconName = "assets/home.png"
        
        self.InitWindow()
        
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.CreateCheckBox()
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        self.show()
        
    def CreateCheckBox(self):
        self.groupBox = QGroupBox("What is your favorite programming Language?")
        self.groupBox.setFont(QtGui.QFont("Sanserif", 13))
        hboxLayout = QHBoxLayout()
        
        self.check1 = QCheckBox("Python")
        self.check1.setIcon(QtGui.QIcon("assets/py.png")) 
        self.check1.setIconSize(QtCore.QSize(38,38))
        # self.check1
        # self.check1
        hboxLayout.addWidget(self.check1)
        
        
        
        
        
if __name__=="__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
    
