from PyQt5.QtWidgets import QApplication, QFormLayout, QPushButton, QRadioButton, QScrollArea, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QButtonGroup, QGroupBox
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
        
        gbox = QGroupBox("This is a group box")
        formlayout = QFormLayout()
        
        
        lblList = []
        btnList = []
        val = 20
        for i in range(val):
            lblList.append(QLabel("Label"))
            btnList.append(QPushButton("Click me")) 
            formlayout.addRow(lblList[i], btnList[i])
            
        gbox.setLayout(formlayout)
        
        scrol = QScrollArea()
        scrol.setWidget(gbox)
        scrol.setWidgetResizable(True)
        scrol.setFixedHeight(400)
        
        qvbx = QVBoxLayout()
        qvbx.addWidget(scrol)
        self.setLayout(qvbx)
        
        
            
        
        
        
        self.show()
        
    
if __name__=="__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
    

        
   