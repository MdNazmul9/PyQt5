from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QButtonGroup
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
        hbox = QHBoxLayout()
        
        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        hbox.addWidget(self.label)
        
        self.buttongroup = QButtonGroup()
        self.buttongroup.buttonClicked[int].connect(self.on_button_clicked)
        
        button = QPushButton("python")
        self.buttongroup.addButton(button,1)
        button.setIcon(QtGui.QIcon("assets/py.png"))
        button.setIconSize(QtCore.QSize(40,40))
        hbox.addWidget(button)
        
        button = QPushButton("CPP")
        button.setIcon(QtGui.QIcon("assets/cpp.png"))
        button.setIconSize(QtCore.QSize(40,40))
        self.buttongroup.addButton(button,2)
        hbox.addWidget(button)
        
        button = QPushButton("CS")
        button.setIcon(QtGui.QIcon("assets/cs.png"))
        button.setIconSize(QtCore.QSize(40,40))
        self.buttongroup.addButton(button,3)
        hbox.addWidget(button)
        
        self.setLayout(hbox)
        self.InitWindow()
        
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()
        
    def on_button_clicked(self, id):
        for button in self.buttongroup.buttons():
            if button is self.buttongroup.button(id):
                self.label.setText(button.text()+ " was clicked")
            
        
    
if __name__=="__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
    

        
   