# MainWindow.py
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from PyQt5 import QtCore, QtGui

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Window"
        self.top = 100
        self.left = 10
        self.width = 720
        self.height = 600
        self.InitWindow()
        
    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("assets/home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
     
     
        
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
        