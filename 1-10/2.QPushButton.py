from PyQt5.QtWidgets import QApplication, QPushButton ,QMainWindow
import sys
from PyQt5 import QtCore, QtGui

from PyQt5.QtCore import QRect



class Window(QMainWindow):
    def __init__(self):
        super().__init__() # important
        
        title = "PyQt5 Push Button"
        left = 500
        top = 200
        width = 300
        height = 250
        iconName = "assets/home.png"
        
        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, top, width, height )
        self.UiComponents()
        self.show() # important 
    
    def  UiComponents(self):
        button = QPushButton("Click Me", self)
        # button.move(50,50)
        button.setGeometry(QRect(100, 100,  112, 50))
        # button.setIcon(QtGui.QIcon("assets/home.png"))
        # button.setIconSize(QtCore.QSize(40,40))
        

if __name__=="__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
