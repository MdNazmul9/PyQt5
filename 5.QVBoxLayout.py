from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QVBoxLayout #QMainWindow
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
        self.iconName = "home.png"
        self.InitWindow()
        
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.weidth, self.height)
        self.show()
        
        
        
if __name__=="__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
   
