# MAD LIBS GENERATOR, by John S.
# circa 2015

#FUNCTIONS (each one controls a madlib routine)

# import only system from os
from os import system, name
# import sleep to show output for some time period
from time import sleep
def clear():
	# for windows
	if name == 'nt':
		_ = system('cls')
	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')

def  albert():
    """A Place:
    Adjective #1:
    Adjective #2:
    Female Celebrity:
    Male Celebrity:
    Noun #1:
    Noun #2:
    Noun #3:
    Plural Noun #1:
    Plural Noun #2:
     Plural Noun #3:
    Plural Noun #4:
    Plural Profession:
    """
    print("First, please enter the following...")
    place = input("A Place: ")
    a1 = input("Adjective #1: ")
    a2 = input("Adjective #2: ")
    a3 = input("Adjective #3: ")
    fem = input("Female Celebrity: ")
    male = input("Male Celebrity: ")
    n1 = input("Noun #1: ")
    n2 = input("Noun #2: ")
    n3 = input("Noun #3: ")
    pn1 = input("Plural Noun #1: ")
    pn2 = input("Plural Noun #2: ")
    pn3 = input("Plural Noun #3: ")
    pn4 = input("Plural Noun #4: ")
    profs = input("Plural Profession: ")

    print("--------------------------------------------------------------------")
    print("Albert Einstein, the son of "+male+" and "+fem+",")
    print("was born in Ulm, Germany, in 1879. In 1902, he had a job")
    print("as assistant "+n1+" in the Swiss patent office and attended")
    print("the University of Zurich. There he began studying atoms, molecules,")
    print("and "+pn1+". He developed the theory of")
    print(a1+" relativity, which expanded the phenomena of sub-atomic")
    print(pn2+" and "+a2+ " magnetism. In 1921,")
    print("he won the Nobel prize for "+pn3+" and was director of")
    print("theoretical physics at the Kaiser Wilhelm "+n2+" in Berlin.")
    print("In 1933, when Hitler became Chancellor of "+place+",")
    print("Einstein came to America to take a post at Princeton Institute for")
    print(pn4 +", where his theories helped America devise the first")
    print("atomic "+n3+". There is no question about it: Einstein was")
    print("one of the most brilliant "+profs+" of our time.")
    print("--------------------------------------------------------------------")
    input("Enter any text to continue...")

def  bullfight():
    """docstring"""
    print("Work In Progress!")
    sleep(4)

def  hamlet():
    """docstring"""
    print("Work In Progress!")
    sleep(4)

def  QandA():
    """docstring"""
    print("Work In Progress!")
    sleep(4)

def  ToWhom():
    """docstring"""
    print("Work In Progress!")
    sleep(4)




#First select one of several Mad libs (from RedKid.net)

while True:
    print(""" 
    -------------------------------------------------
             MAD - LIBS GENERATOR, by John Smith
    -------------------------------------------------
    """)
    print("Please Select from one of the following MadLibs:")
    print("""
    1.) Albert Einstein
    2.) Bull Fighting
    3.) Hamlet
    4.) Medical Q and A
    5.) To Whom It May Concern
    6.) [Exit the Program]
    """)
    choice = int(input("Enter a Number: "))
    if choice==1:
        albert()
        clear()
    elif choice ==2:
        bullfight()
        clear()
    elif choice ==3:
        hamlet()
        clear()
    elif choice ==4:
        QandA()
        clear()
    elif choice ==5:
        ToWhom()
        clear()
    elif choice ==6:
        quit()

