''' PSEUDO-RANDOM NUMBER GENERATOR:
   By: John H. Smith, aka johnhs3. ca. 2019
   Creates a list of random numbers using Additive Lagged Fibonacci algorithm.
    Current seed: {j=418, k=1729, M=42}. So, max period length is given by:
    ((2^k)-1)*2^(M-1)

    Will add vectors and an option for different starting seeds j and k
    later, not that it matters lol

    Other ideas:
    -Range control
    -Restrict Starter values
    -Chain PNRGs for better starter values
    -Options to choose pairs (j,k)

'''
#Warning: Do NOT use this! It is horrendous and makes me depressed

import math

M = 42
j = 418
k = 1729
Sa=0
Sb=0
Sn=0

def alfg(): #iterates alfg generating one "random" number
    global Sn
    global Sa
    global Sb
    Sb = Sa
    Sa = Sn
    Sn = (Sa+Sb)%(2^M) #Bruh what is this. alfg(2,7) gives ALL even numbers :(
                    #ANS>: I THINK I KNOW. DON't use ANY powers of 2 for a n b.
    return Sn       #Also, iteration 1 and 2 are always the same val. WHY?
                    #Answer: B/c init of Sa n Sb = 0. t/f it's adding nothing the first 2 iterations.
def main():
    global Sn
    global Sa
    global Sb
    print("=============================================================")
    print("Additive Lagged Fibonacci RNG: John S. \n")
    print("Generates n random numbers from starting values Sa and Sb,")
    print("=============================================================")
    
    print("Enter # of RN's to generate: ") #gets input
    num = int(input("num: "))
    print("Enter Starting Vals for Sa and Sb: ")
    Sa = int(input("Sa: "))
    Sb = int(input("Sb: "))
    for i in range(num): #Iterates alfg() n times. 
        print(str(alfg()))
    return None

main()
    
