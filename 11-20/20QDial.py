from PyQt5.QtWidgets import QApplication, QDial, QPushButton, QRadioButton, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QButtonGroup, QGroupBox
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
        vbx = QVBoxLayout()
        
        
        self.lbl = QLabel(self)
        self.lbl.setFont(QtGui.QFont("Sanserif", 15))
        vbx.addWidget(self.lbl)
        
        
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(30)
        self.dial.valueChanged.connect(self.dialChanged)
        
        
        
        vbx.addWidget(self.dial)
        self.setLayout(vbx)
        # self.setLayout(self.lbl)
        self.show()
        
    def dialChanged(self):
        getValue = self.dial.value()
        self.lbl.setText("Dial changed value"+str(getValue))
    
if __name__=="__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
    

        
   