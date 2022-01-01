from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QDialog, QGroupBox, QVBoxLayout #QMainWindow
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QRect



class Window(QDialog):
    def __init__(self):
        super().__init__()
        
        self.title = "PyQt5 Grid Layout"
        self.left = 500
        self.top = 200
        self.weidth = 400
        self.height = 100
        self.iconName = "assets/home.png"
        self.InitWindow()
        
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.weidth, self.height)
        self.CreateLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        
        self.show()
        
    def CreateLayout(self):
        self.groupBox = QGroupBox("What is your favorite programming language?")
        gridLayout = QGridLayout()
        
        button = QPushButton("Python", self)
        button.setIcon(QtGui.QIcon('assets/py.png'))
        button.setIconSize(QtCore.QSize(38,38))
        button.setMinimumHeight(40)
        gridLayout.addWidget(button, 0, 0)
        
        button1 = QPushButton("C", self)
        button1.setIcon(QtGui.QIcon('assets/c.png'))
        button1.setIconSize(QtCore.QSize(38,38))
        button1.setMinimumHeight(40)
        gridLayout.addWidget(button1, 0, 1)
        
        
        button2 = QPushButton("Csharp", self)
        button2.setIcon(QtGui.QIcon('assets/cs.png'))
        button2.setIconSize(QtCore.QSize(38,38))
        button2.setMinimumHeight(40)
        gridLayout.addWidget(button2, 1, 0)
        
        
        button3 = QPushButton("CPP", self)
        button3.setIcon(QtGui.QIcon('assets/cpp.png'))
        button3.setIconSize(QtCore.QSize(38,38))
        button3.setMinimumHeight(40)
        gridLayout.addWidget(button3, 1, 1)
        
        
        self.groupBox.setLayout(gridLayout)
        
        
        
if __name__=="__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
   
