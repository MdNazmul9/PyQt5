from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect

class Window(QDialog):
    def __init__(self):
        super().__init__()
        
        self.title = "Label" 
     
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
        
        vbox = QVBoxLayout()
        label = QLabel("This is first label")
        vbox.addWidget(label)
        
        label2 = QLabel("This is second label")
        
        label2.setFont(QtGui.QFont("Sanserif", 20))
        label2.setStyleSheet('color:red')
        vbox.addWidget(label2)
        
        self.setLayout(vbox)
        
        self.show()
        
if __name__=="__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
    

        
        
    