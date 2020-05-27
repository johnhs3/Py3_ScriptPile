#Yes, I should prob do a better job of commenting my code. OKAY, Fine, here it goes:::
""" ==============================================================================
NATO CODE CONVERTER, By John H. Smith
Original version: May 2017
*** Edited in May 2020 to add to repo. Github: johnhs3***

This program just does the military-speak thing. Run it and see. :)
===================================================================================
"""

codesrc = {"A": "ALPHA" ,
           'B': 'BRAVO' ,
           'C': 'CHARLIE',
           'D': 'DELTA',
           'E': 'ECHO',
           'F': 'FOXTROT',
           'G': 'GOLF',
           'H': 'HOTEL',
           'I': 'INDIA',
           'J': 'JULIETT',
           'K': 'KILO',
           'L': 'LIMA',
           'M': 'MIKE',
           'N': 'NOVEMBER',
           'O': 'OSCAR',
           'P': 'PAPA',
           'Q': 'QUEBEC',
           'R': 'ROMEO',
           'S': 'SIERRA',
           'T': 'TANGO',
           'U': 'UNIFORM',
           'V': 'VICTOR',
           'W': 'WHISKEY',
           'X': 'XRAY',
           'Y': 'YANKEE',
           'Z': 'ZULU',
           '1': 'ONE',
           '2': 'TWO',
           '3': 'THREE',
           '4': 'FOUR',
           '5': 'FIVE',
           '6': 'SIX',
           '7': 'SEVEN',
           '8': 'EIGHT',
           '9': 'NINER',
           '0': 'ZERO'}
while True:
    print("Hello! Welcome to the NATO Phonetic Alphabet Code Converter.")
    print("This pgrm allows you to feed in an input string, then converts")
    print("it to a phonetic string and prints the result.")
    user_inp = input("Enter your string: ")
    toUpperC = user_inp.upper()         #makes uppercase for standardization
    newstr = ""

    for i in range(0,len(toUpperC),1):      # Computes the new string based on input
        current = toUpperC[i:i+1]
        if codesrc.get(current) == None:
            newstr += current + "-"         #NOTE: The LAST Character Also has a hyphen as well! GET RID OF THIS!!! ***
        else:
            newstr += codesrc[current]
            if current == " ":      #If the current char is a space, DON't add a hyphen ("-") in between!
                continue
            else:
                newstr += "-"

    print("====================================================================")
    print("Your Output String is: ")
    print(newstr)
    print("====================================================================")
    print("Options: ")
    print('1) Convert Another')
    print('2) Quit')

    choice = input("Enter choice: ")
    while True:         #This loop allows for re-entry of other strings or quitting.
        if choice == '1':
            break
        elif choice == '2':
            exit()
        else:
            choice = input("Invalid. Please enter again: ")

