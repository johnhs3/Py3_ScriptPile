'''=========== Wave Generator Program: John H. Smith ===========
Original: May 2018
This will make a nice lil wave on your screen, and allow you to change the parameters like Amplitude and Frequency.

***EDITED May 2020 for Github. Github: johnhs3
'''

import time
import keyboard

amp = 10
freq = 0.5

def wave():
    while True:
            for i in range(amp):
                 if keyboard.is_pressed('return'):
                     exit()
                 else:
                     time.sleep(1/(2*amp*freq))  # Still dk how to do this w/o busy waiting. Should learn how to do this ASAP.
                     print("#"*i)           #Also something doesn't seem right about the above. YEAHHH this DEFINITELY isn't working correctly!!!
            for i in range(amp,1,-1):
                if keyboard.is_pressed('return'):
                    exit()
                else:
                    time.sleep(1/(2*amp*freq))
                    print("#"*i)

def printBlurb():
    print("------------Wave Generator v 1.0 ------------")
    print("Directions: Press SPACE to start the wave.")
    print("Press ENTER at any time to quit.")
    print("Other options:")
    print("1) Change Amplitude")
    print("2) Change Frequency")
    print("3) Quit now")
printBlurb()
while True: #Begin Main Loop of program
    if keyboard.is_pressed('space'):    
            wave()  #calling functions seems to be the best way to do this. ??
    elif keyboard.is_pressed('1'):
        print("Enter Desired Amplitude of Wave: ")
        amp = int(input())
        printBlurb()
        continue
    elif keyboard.is_pressed('2'):
        print("Enter Desired Frequency of Wave: ")
        freq = int(input())
        printBlurb()
        continue
    elif keyboard.is_pressed('3'):
        break

#Okay, WHAT is going on with the wave??? The keyboard input seems to be REALLY finicky! Like half the time it doesn't work or something.
#Perhaps the other issue is because we're actually hitting the maximum speed of python execution on this computer.











    

    




        
