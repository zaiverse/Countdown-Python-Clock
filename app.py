import sys
from PyQt6.QtCore import QTimer,QDateTime
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QFrame, QGridLayout, QTabWidget

class CountdownClock(QWidget):

    def __init__(self):
        super().__init__()

        # Create grid layouts
        self.mainlayout = QGridLayout()
        self.grid = QGridLayout()

        #Timer tab
        timeSelectLayout = QVBoxLayout()
        timeLabelLayout = QVBoxLayout()
        timerLayout = QVBoxLayout()
        self.timerTab = QWidget()
        self.timerTab.setLayout(timerLayout)
        #Tab widget
        self.tabs = QTabWidget()

        # Rows for selection menu of time
        self.firstRow = 0
        self.secondRow = 1
        self.thirdRow  = 2

        # Columns for selection menu of time
        self.firstCol = 0
        self.secondCol = 1
        self.thirdCol = 2
        # Row where number selection is located
        self.rowOfNum = 1

        # Create menu selection
        for i in range(3):
            # Increase number buttons
            self.createButton("^",self.firstRow,i)
            # Number labels
            self.createLabel("0",self.secondRow,i)
            # Decrease number buttons
            self.createButton("-",self.thirdRow,i)

        # Create time label
        self.timeLabel = QLabel("00:00:00")
        timeLabelLayout.addWidget(self.timeLabel)

        self.timer = QTimer()

        # Create submit button and add event 
        self.selectTime = QPushButton("Submit")
        self.selectTime.clicked.connect(self.getTime)

        timerLayout.addLayout(timeLabelLayout)            
        timerLayout.addLayout(self.grid)

        timeSelectLayout.addWidget(self.selectTime)
        timerLayout.addLayout(timeSelectLayout)

        self.tabs.addTab(self.timerTab, 'Timer')
        self.mainlayout.addWidget(self.tabs)

        self.setLayout(self.mainlayout)

    
    # This function creates buttons that allows access to their row and column placement
    def createButton(self,text,row,col):
        button = QPushButton(text,self)
        self.grid.addWidget(button,row,col)
        button.clicked.connect(lambda _, r=row, c=col: self.updateLabel(r, c))

    # Function accesses button row and column to update the time label
    def updateLabel(self,r,c):
        # If a button which increments the time was clicked
        # Access the labels row and column
        if(r==self.firstRow):
            label = self.grid.itemAtPosition(self.rowOfNum,c).widget()
            content = int(label.text())
            # Seconds and minutes must not be over 60 
            if(c==self.secondCol or c==self.thirdCol):
                if(content < 59):
                    content += 1
            # However, hours will not have a limit for now
            else:
                content += 1

            label.setText(str(content))
        
        # If a button which decrements the time was clicked
        # Access the labels row and column
        elif(r==self.thirdRow):
            label = self.grid.itemAtPosition(self.rowOfNum,c).widget()
            content = int(label.text())
            # Time must not be a negative value
            if(content > 0):
                content -= 1
                label.setText(str(content))

    # Function creates a label
    def createLabel(self,text,row,col):
        label = QLabel(text,self)
        self.grid.addWidget(label,row,col)

    # Function gets access to the time which user has selected to count down from
    def getTime(self):
        # Disable submit button
        self.selectTime.setEnabled(False)

        for i in range(3):
            label = self.grid.itemAtPosition(self.rowOfNum,i).widget()
            content = int(label.text())

            if(i == self.firstCol):
                hours = content
            elif(i == self.secondCol):
                minutes = content
            else:
                seconds = content

        # Update label with user selected hours, minutes, and seconds
        self.setDisplay(hours,minutes,seconds)
        # Calculate full time and start timer
        self.fullTime = hours * 3600 + minutes * 60 + seconds
        self.timer.timeout.connect(self.countdown)
        self.timer.start(1000)    

    # This function updates time label
    def setDisplay(self,h,m,s):

        self.timeLabel.setText("{:02}:{:02}:{:02}".format(int(h), int(m), int(s)))

    # Function runs countdown until time has ran out
    def countdown(self):
        # If time is greater than zero 
        # Continue to decrement value and update time label
        if(self.fullTime > 0):
            self.fullTime -= 1
            minutes,seconds = divmod(self.fullTime, 60)
            hours,minutes = divmod(minutes,60)

            self.setDisplay(hours,minutes,seconds)
        # Stop timer once time is equal to zero
        else:
             self.timer.stop()
             # Reactivate submit button
             self.selectTime.setEnabled(True)


app = QApplication(sys.argv)

window = CountdownClock()
window.show()

app.exec()