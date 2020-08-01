''' PSEUDO-RANDOM NUMBER GENERATOR:
   By: John H. Smith, aka johnhs3. ca. 2019
   Generates a random number digit between 0 and 9 using
   the Linear Congruential generation algorithm. Can also
   interpolate to different ranges of values fairly easily
   thru arithmetic.

   Functionality will be expanded later to include multiple algorithms.
'''

import math

a = 1664525
c = 1013904223
m = 2^32
seed = 13334564589

def lcg(aval,cval,modval,seedval):
    seed = (aval*seedval+cval)%modval
    return seed

def main():
    print("Enter # of RN's to generate: ")
    num = int(input())
    for i in range(num):
        print(str(lcg(a,c,m,seed+1)))
    return None

main()
    
