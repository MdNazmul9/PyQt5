from PyQt5.QtWidgets import QApplication, QDialog, QLabel
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect

class Window(QDialog):
    def __init__(self):
        super().__init__()
        
        self.title = "Label" 
        self.left = 200
        self.top = 400
        self.weidth = 600
        self.hight = 400
        self.iconName = "assets/home.png"
        
        self.InitWindow()
        
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.weidth, self.hight)
        
        self.show()
        
if __name__=="__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
    
    
        
        
    