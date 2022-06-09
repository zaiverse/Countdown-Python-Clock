import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QWidget

class Practice(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.setLayout(self.layout)

        self.frame1()

    def frame1(self):   
        firstVecticalCol = QVBoxLayout()
        secondVecticalCol = QVBoxLayout()
        thirdVecticalCol = QVBoxLayout()

        print("IN here!")
        button1 = QPushButton("^")
        firstVecticalCol.addWidget(button1)

        button2 = QPushButton("-")
        firstVecticalCol.addWidget(button2)

        button3 = QPushButton("^")
        secondVecticalCol.addWidget(button3)

        button4 = QPushButton("-")
        secondVecticalCol.addWidget(button4)

        button5 = QPushButton("^")
        thirdVecticalCol.addWidget(button5)

        button6 = QPushButton("-")
        thirdVecticalCol.addWidget(button6)

        self.horizontal.addLayout(firstVecticalCol)
        self.horizontal.addLayout(secondVecticalCol)
        self.horizontal.addLayout(thirdVecticalCol)
        self.layout.addLayout(self.horizontal)




app = QApplication(sys.argv)

window = Practice()
window.show()

app.exec()