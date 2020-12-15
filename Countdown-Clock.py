#import time module
import time
import datetime

def countdown(m,s):

    #set clock to true
    clock = True

    while clock:
        timer = datetime.timedelta(minutes=m,seconds=s)

        print(timer, end="\r")
        if s == 0 and m != 0:
            m -= 1
            s = 60
        elif m == 0 and s == 0:
            clock = False
        else:
            s -= 1
            time.sleep(1)

#ask user for hour(s), minute(s), and second(s) they would like to count down from
print("Welcome to clock world!")

#handles user input
def begin():
    
    userInput = True

    #loop until user enters integer only for both minutes and seconds
    while userInput:
        m = input("Enter minute(s): ")
        s = input("Enter second(s): ")

        try:
            minutes,seconds =  int(m), int(s)
            #call countdown funtion
            countdown(minutes,seconds)

            #exit loop
            userInput = False
        except:
            print("You entered something wrong")


begin()