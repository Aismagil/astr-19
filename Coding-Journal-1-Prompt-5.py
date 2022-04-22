#This program will write 
#out a table of the function sin(x) vs x,
#where x is tabulated between 0 and 2pi
#with a thousand entries.

#import numpy
import numpy as np


#defines the main() function 
def main():
    x = np.linspace(0,2*np.pi,1000)            #creates an array of 1000 entries between 0 and 2p
    for i in range(len(x)):
        print(f"{x[i]:6.5e} {np.sin(x[i]):6.5e}")

#executes the main function
if __name__=="__main__":
    main()