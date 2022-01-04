from PyQt5.QtWidgets import QApplication,QLineEdit, QHBoxLayout, QPushButton, QWidget,QDialog, QLabel, QVBoxLayout
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect

from PyQt5.QtGui import QPixmap
class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.title = "PyQt5 Line Edit" 
     
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
        
        
        self.lineedit = QLineEdit(self)
        self.lineedit.setFont(QtGui.QFont("Sanserif", 15))
        #onPressed
        self.lineedit.returnPressed.connect(self.onPressed)
        hbox.addWidget(self.lineedit)
        
        self.label = QLabel(self)
        hbox.addWidget(self.label)
        
        
        # btn = QPushButton("Click me", self)
        # btn.setWhatsThis("Display at when press shift+f1 and focus it")
        # hbox.addWidget(btn)
        
        self.setLayout(hbox)
        self.show()
        
       
    def onPressed(self):
        self.label.setText(self.lineedit.text())
    
        
if __name__=="__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
    

        
   