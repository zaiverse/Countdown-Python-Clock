import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFrame, QGridLayout

class Practice(QWidget):

    def __init__(self):
        super().__init__()

        self.grid = QGridLayout()

        self.createButton("Hello",1,1)
        self.createButton("yikes",1,2)
        self.setLayout(self.grid)

    def createButton(self,text,col,row):

        button = QPushButton(text)
        self.grid.addWidget(button,col,row)



app = QApplication(sys.argv)

window = Practice()
window.show()

app.exec()