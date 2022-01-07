from PyQt5.QtWidgets import QApplication, QFrame, QLineEdit, QSlider, QSplitter, QPushButton, QRadioButton, QSplitter, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QButtonGroup, QGroupBox
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect, Qt, left

from PyQt5.QtGui import QPixmap
class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.title = "PyQt5 QSlider" 
     
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "assets/home.png"
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        hbox = QHBoxLayout()
        
        self.slider = QSlider()
        
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.valueChanged)
        hbox.addWidget(self.slider)
        
        self.label = QLabel("0")
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        hbox.addWidget(self.label)
                
        
        self.setLayout(hbox)
        
        self.show()
        
    def valueChanged(self):
        size = self.slider.value()
        self.label.setText(str(size))
    
    
    
if __name__=="__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
    

        
   