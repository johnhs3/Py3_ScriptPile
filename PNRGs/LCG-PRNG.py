''' PSEUDO-RANDOM NUMBER GENERATOR:
   By: John H. Smith, aka johnhs3. ca. 2019
   Generates a random number digit between 0 and 9 using
   the Linear Congruential generation algorithm. Can also
   interpolate to different ranges of values fairly easily
   thru arithmetic.
   Functionality will be expanded later to include multiple algorithms.

   Also:
   -Range restriction (somehow?)
   -another rng to make seeds
'''
#WARNING: This is terrible and broken. Don't use it. I'll make it better at a later date

import math

a = 1664525
c = 1013904223
m = 2^32
seed2 = 13334564589
seed = 123456789 #init values.

def lcg():
    global seed
    global a
    global c
    global m
    seed = (a*seed+c)%m #Goes in a cycle every 6 terms!!! >:( What do?
    return seed

def main():
    print("Enter # of RN's to generate: ")
    num = int(input())
    for i in range(num):
        print(str(lcg()))
    return None

main()
