''' PSEUDO-RANDOM NUMBER GENERATOR:
   By: John H. Smith, aka johnhs3. ca. 2019
   Creates a list of random numbers using Blum Blum Shub algorithm.
   Takes n as input, number of rn's to generate.
   Probably my favorite PNRg i've implemented thusfar. It's easy,
   fast and seems to work like a charm.

    Would recommend making a list / vector of good seeds.

    Also:
    -Truncate extra digits as an option
    -seperate into several rn's (restrict range)
    -
    -wow

'''

p = 30000000091
q = 40000000003
m = p*q

xn1 = 9065091811
xn = 9065091811 #starter value for xn.

def bbs(): #iterates alfg generating one "random" number
    global xn1
    global xn
    global m
    xn = xn1
    xn1 = ((xn)**2)%(m)
    return xn1


    
def main():
    print("=============================================================")
    print("Blum Blum Shub Pseudo RNG: John S.")
    print("=============================================================")
    
    print("Enter # of RN's to generate: ") #gets input
    num = int(input("num: "))
    for i in range(num): #Iterates alfg() n times. 
        print(str(bbs()))
    return None

main()
    
