from PyQt5.QtWidgets import QApplication, QPushButton, QRadioButton, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QButtonGroup, QGroupBox
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect

from PyQt5.QtGui import QPixmap
class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.title = "PyQt5 QButtonGroup" 
     
        self.left = 300
        self.top = 400
        self.width = 400
        self.height = 100
        self.iconName = "assets/home.png"
        
        self.InitWindow()
        
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        hbox = QHBoxLayout()
                
        groupbox = QGroupBox("Select your favorite fruit")
        groupbox.setFont(QtGui.QFont("Sanserif", 15))
        
        hbox.addWidget(groupbox)
        
        vbox = QVBoxLayout()
        
        rad1 = QRadioButton("Apple")
        vbox.addWidget(rad1)
        
        rad2 = QRadioButton("Banana")
        vbox.addWidget(rad2)
        
        rad3 = QRadioButton("Melon")
        vbox.addWidget(rad3)
        
        groupbox.setLayout(vbox)
        
        self.setLayout(hbox)
        self.show()
        
    
if __name__=="__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
    

        
   