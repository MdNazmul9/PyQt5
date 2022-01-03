from PyQt5.QtWidgets import QApplication, QDialog, QGroupBox, QHBoxLayout, QLabel, QRadioButton, QVBoxLayout, QLabel
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect

from PyQt5.QtGui import QPixmap
class Window(QDialog):
    def __init__(self):
        super().__init__()
        
        self.title = "pyQT5" 
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
        
        self.radioButton()
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        
        self.label = QLabel()
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        vbox.addWidget(self.label)
        
        self.setLayout(vbox)
        
        self.show()
        
    def radioButton(self):
        self.groupBox = QGroupBox("What is your favorite game?")
        self.groupBox.setFont(QtGui.QFont("Sanserif", 13))
        hboxlayout = QHBoxLayout()
        
        self.rediobtn1 = QRadioButton("Football")
        self.rediobtn1.setChecked(True)
        self.rediobtn1.setIcon(QtGui.QIcon("assets/football.jpeg"))
        self.rediobtn1.setIconSize(QtCore.QSize(30,30))
        self.rediobtn1.toggled.connect(self.OnRadioBtn)
        hboxlayout.addWidget(self.rediobtn1)
        
        self.rediobtn2 = QRadioButton("Cricket")
        self.rediobtn2.setIcon(QtGui.QIcon("assets/cricket.png"))
        self.rediobtn2.setIconSize(QtCore.QSize(30,30))
        self.rediobtn2.toggled.connect(self.OnRadioBtn)
        hboxlayout.addWidget(self.rediobtn2)
        
        self.rediobtn3 = QRadioButton("Tennis")
        self.rediobtn1.setChecked(True)
        self.rediobtn3.setIcon(QtGui.QIcon("assets/tennis.jpeg"))
        self.rediobtn3.setIconSize(QtCore.QSize(30,30))
        self.rediobtn3.toggled.connect(self.OnRadioBtn)
        hboxlayout.addWidget(self.rediobtn3)
        
        self.groupBox.setLayout(hboxlayout)
        
    def OnRadioBtn(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.label.setText("You have select "+ radioBtn.text())
            
    
if __name__=="__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
    

        
        
    