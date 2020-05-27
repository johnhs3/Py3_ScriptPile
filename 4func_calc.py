'''
A simple calculator, by John S. Date:  Mar. 19, 2017
*** Edited May 2020 for Github Repo! Github: johnhs3***
'''
while True:
    print('Options:')
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print("5) Quit")
    user_input=input("Enter: ")

    if user_input == "5":
        break
    elif user_input == "1":
        a=float(input("A:"))
        b=float(input("B:"))
        res = str(a+b)
        print("Answer:"+res)
    elif user_input == "2":
        a=float(input("A:"))
        b=float(input("B:"))
        res = str(a-b)
        print("Answer:"+res)
    elif user_input == "3":
        a=float(input("A:"))
        b=float(input("B:"))
        res = str(a*b)
        print("Answer:"+res)
    elif user_input == "4":
        a=float(input("A:"))
        b=float(input("B:"))
        if(b==0): print("Divide by Zero!")
        else:
            res = str(a+b)
            print("Answer:"+res)
    else:
        print("Unknown input")
