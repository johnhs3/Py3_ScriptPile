import time
import keyboard

def pause():
    while True:
        if keyboard.is_pressed('space'): #Still don't know how to avoid busy waiting!!!
            return #Probably something to look up next

def wave():
    while True:
            for i in range(10):
                 if keyboard.is_pressed('return'):
                     printBlurb()
                     return
                 elif keyboard.is_pressed('space'):
                     pause()
                 else:
                     time.sleep(0.1)  # More Busy Waiting!!! >:(
                     print("#"*i)
            for i in range(10,1,-1):
                if keyboard.is_pressed('return'):
                    printBlurb()
                    return
                elif keyboard.is_pressed('space'):
                    pause()
                else:
                    time.sleep(0.1)
                    print("#"*i)

def printBlurb():
   print("------------Wave Generator v 1.0 ------------")
   print("Directions: Press SPACE to start, and again to pause.")
   print("Press ENTER at any time to return here.")
   print("Other options:")
   print("1) Change Amplitude")
   print("2) Change Speed of oscillation")
   print("3) Quit now")

#==========================================================================
printBlurb()   
while True:
       if keyboard.is_pressed('space'):
           wave()
       elif keyboard.is_pressed('1'):
           print("AAAA")
       elif keyboard.is_pressed('2'):
           print("SPEED")
       elif keyboard.is_pressed('3'):
           break












    

    




        
