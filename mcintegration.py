'''
BY JOHN S., aka johnhs3. CA. 2020
A simple Monte-Carlo Integration schema for finding the area of a shaded region relative to some 2d, rectangular domain.
To use it just place an image (B&W only, crisp edges on region) into the same dir. as the script, then run.

ideas for later:
-Axes: In another color (maybe red), make it so that you can place a set of axes in your images and the MC counter won't
count any of them
-Duplicate the image, mark each pixel that was sampled with another color? (Cool visualization)
-
-Aspect ratio checker: Checks whether the domain you entered maintains the same ar relative to pixel
width/height (within some epsilon for fencepost), then returns a warning if they're not the same.
-

'''

from PIL import Image
import random

def main():
    print("============================================================================")
    print("MONTE CARLO INTEGRATION SCHEME FOR SIMPLE RECTANGULAR DOMAINS: By John S.")
    print("============================================================================")
    print("Input some data: ")
    filename = input("Filename(Must be in same directory as script):") #Yes.
    print("Dim. of Domain: ")
    Lx = float(input("x-min: ")) #Gets the upper and lower boundss for rect domain.
    Hx = float(input("x-max: "))
    Ly = float(input("y-min: "))
    Hy = float(input("y-max: "))
    print("Num Samples: ")
    n = int(input("n = ")) #Gets n, # samples to use in trial
    img = Image.open(filename)
    print("Computing... (WARNING: This f'n is slow. May take awhile)")
    img.show()
    w, h = img.size
    inr=0
    outr=0
    prop = 0
    '''It is true that the f'n, starting immediately after this, is quite slow.
From what I've seen online, the getpixel method may be the problem. We'll have
to figure out a way to use something else... but of course, large n will still
cause slowdowns.'''
    for i in range(n):
        coords=x,y= random.uniform(0,w-1),random.uniform(0,h-1)
        curpixel = img.getpixel(coords)
        if curpixel < 250: #Threshold for light vs. dark is arbitrary. PLEASE Use regions with clear borders / no Anti-aliasing for input region! Or else it'll work like sh*t
            inr = inr+1
        else:
            outr = outr+1
    prop = inr/n #Le magic sauce
    domArea = (Lx+Hx)*(Ly+Hy) #scale by domain.
    area=prop*domArea
    '''DEBUG:
    print(str(n))
    print(str(inr))
    print(str(outr))
    print(str(prop))
    print(str(domArea))
    '''
    print("Result: Area: "+str(area))


if __name__ == "__main__":
    main()
