'''
    A text analysis program that reads from a file and finds useful stuff.
    Based on sketch in SoloLearn.
    By John Smith, Date: June 2017
    ***EDITED May 2020 for Github: Git: johnhs3***
'''
#NOTE (Added Later): This program has poor handling of keyboard input. It'd be nice to be able to make the previously entered key disappear from the prompt
# so that it doesn't mess up the file name input or anything else.


import keyboard

def printblurb():   #we need this for 
    print("===================== Text Analyzer 3000!!! =====================")
    print("This program can read a text file from the same directory and give you useful info about it.")
    print("What do you want to do? :")
    print("1) Get length of file")
    print("2) Get # spaces in file")
    print("3) Percentages of each char in file")
    print("4) Search for a substring. Returns # of instances of that substring and pos. of first instance")
    print("5) Quit.")

def count_char(text,char): #Counts occurrences of certain character in string text'''
    count=0
    for c in text:
        if c==char:
            count+=1
    return count

def length():   #Outputs the length of the textfile'''
    filename = input("Enter a filename: ")  #It must be in same file folder!
    with open(filename) as f:
        text = f.read()
        print("=================================================================") #formatting :)
        print("Length of file (char): " +str(len(text)))
    printblurb() #Always call printblurb from now on, to "refresh" the program

def numspace(): #Counts the number of spaces present, from which it'd be easy to find word count. I'm not implementing it here.'''
    filename = input("Enter a filename: ")
    with open(filename) as f:
        text = f.read()
        spaces = count_char(text,' ')
        print("=================================================================")
        print("# of spaces: " +str(spaces))
    printblurb()

def percenter(): #Lists percentages that each character makes up for in the total file.'''
    filename = input("Enter a filename: ")
    with open(filename) as f:
        text = f.read()
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890": #NOTE: It would be cool to figure out a way to make Upper and Lowercase count together. Later...?
            percent = 100*count_char(text,char)/len(text)
            print("{0}-{1}%".format(char,round(percent,2))) #Format is unbearable :/
    printblurb()

def search():  #search for a substring in the text. Return the # of times that substring is present, AND the char position of first sighting'''
    filename = input("Enter a filename: ")
    substr = input("Enter a string to look for: ")
    with open(filename) as f:
        text = f.read()
        count = text.count(substr)
        fpos = text.find(substr)
        if(count==0 or fpos==-1): #redundant i guess but wc?
            print("=================================================================")
            print("String not found!")
        else:
            print("=================================================================")
            print("# of instances of Substr: "+str(count))
            print("1st Substr position: "+str(fpos))
    printblurb()

#===================================================================================================== "Main" function:
printblurb()
while True:
    if(keyboard.is_pressed('1')):
        length()
    elif(keyboard.is_pressed('2')):
        numspace()
    elif(keyboard.is_pressed('3')):
        percenter()
    elif(keyboard.is_pressed('4')):
        search()
    elif(keyboard.is_pressed('5')):
        break
