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
        
        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        vbox.addWidget(self.label)
        
        
        self.show()
        
    def CreateCheckBox(self):
        self.groupBox = QGroupBox("What is your favorite programming Language?")
        self.groupBox.setFont(QtGui.QFont("Sanserif", 13))
        hboxLayout = QHBoxLayout()
        
        self.check1 = QCheckBox("Python")
        self.check1.setIcon(QtGui.QIcon("assets/py.png")) 
        self.check1.setIconSize(QtCore.QSize(38,38))
        self.check1.setFont(QtGui.QFont("Sanserif", 13))
        self.check1.toggled.connect(self.OnCheck_Toggled)
        hboxLayout.addWidget(self.check1)
        
        self.check2 = QCheckBox("C")
        self.check2.setIcon(QtGui.QIcon("assets/c.png")) 
        self.check2.setIconSize(QtCore.QSize(38,38))
        self.check2.setFont(QtGui.QFont("Sanserif", 13))
        self.check2.toggled.connect(self.OnCheck_Toggled)
        hboxLayout.addWidget(self.check2)
        
        self.check3 = QCheckBox("CPP")
        self.check3.setIcon(QtGui.QIcon("assets/cpp.png")) 
        self.check3.setIconSize(QtCore.QSize(38,38))
        self.check3.setFont(QtGui.QFont("Sanserif", 13))
        self.check3.toggled.connect(self.OnCheck_Toggled)
        hboxLayout.addWidget(self.check3)
        
        self.check4 = QCheckBox("CS")
        self.check4.setIcon(QtGui.QIcon("assets/cs.png")) 
        self.check4.setIconSize(QtCore.QSize(38,38))
        self.check4.setFont(QtGui.QFont("Sanserif", 13))
        self.check4.toggled.connect(self.OnCheck_Toggled)
        hboxLayout.addWidget(self.check4)
        
        self.groupBox.setLayout(hboxLayout)
        
        
        
    def OnCheck_Toggled(self):
        if self.check1.isChecked():
            self.label.setText("You have select : "+ self.check1.text())
            
        if self.check2.isChecked():
            self.label.setText("You have select : "+ self.check2.text())
        
        if self.check3.isChecked():
            self.label.setText("You have select : "+ self.check3.text())
        
        if self.check4.isChecked():
            self.label.setText("You have select : "+ self.check4.text())
        
       
if __name__=="__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
    
