# PyQt5
### .ui --> .py convert
```
pyuic5 -x ims.ui -o ims_code.py
```
........................................
vbox...................................|
|    groupBox..........................|               
|    |    hboxLayout...................|
|    |    |  checkbox                  |
|    |    |  radiobutton               |
|    |    |  ...                       | 
|    |    |  ...                       |
|    |    |  ...                       |
.......................................|

### Signal
   ##### toggled button radiobutton, checkboxbutton
   ```
   btn.toggled.connect(self.function)
   ```
   ##### ButtonGroup
   ```
   self.buttongroup.buttonClicked[int].connect(self.on_button_clicked)
   ```
        

### hbox and label
```
hbox = QHBoxLayout()
self.label = QLabel(self)
self.label.setFont(QtGui.QFont("Sanserif", 15))
hbox.addWidget(self.label)
self.setLayout(hbox)
```

### button
```
button = QPushButton("CPP")
button.setIcon(QtGui.QIcon("assets/cpp.png"))
button.setIconSize(QtCore.QSize(40,40))
hbox.addWidget(button)
```

### All side increased
........................................
hbox...................................|
|    groupBox..........................|               
|    |    vbox.........................|
|    |    |  checkbox                  |
|    |    |  radiobutton               |
|    |    |  ...                       | 
|    |    |  ...                       |
|    |    |  ...                       |
.......................................|

