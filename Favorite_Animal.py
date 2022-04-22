#This program will declare a class describing my favorite animal.

#import sys
import sys

class Animal:

    # a class describing my favorite animal

    def print(self):
        print("This is the animal description")
        print(f"Length of arms = {self.arm_length}")
        print(f"Length of legs = {self.leg_length}")
        print(f"Number of eyes = {self.num_eyes}")
        print(f"It has a tail ? {self.has_tail}")
        print(f"It is furry ? {self.is_furry}")

    def __init__(self,arml=0.0,legl=0.0,neyes=2,tail=True,furry=False):
        self.arm_length   = arml
        self.leg_length   = legl
        self.num_eyes     = neyes
        self.has_tail     = tail
        self.is_furry     = furry


#This defines the main function
def main():
    
    #set default number of lengths,
    #numbers, and booleans
    arml=0.0
    legl=0.0
    neyes=2
    tail=True
    furry=False

    #if there are at least 2 command
    #line arguments, set arml equal
    #to the second
    if(len(sys.argv)>=2):
        arml = float(sys.argv[1])

    #if there are 3 command line
    #arguments, set legl equal
    #to the third
    if(len(sys.argv)>=3):
        legl = float(sys.argv[2])

    #if there are at least 4 command
    #line arguments, set neyes equal
    #to the fourth
    if(len(sys.argv)>=4):
        neyes = int(sys.argv[3])

    #if there are 5 command line
    #arguments, set tail equal
    #to the fifth
    if(len(sys.argv)>=5):
        tail= bool(sys.argv[4])

    #if there are 6 command line
    #arguments, set furry equal
    #to the sixth
    if(len(sys.argv)>=6):
        tail= bool(sys.argv[5])

    #initialize our animal
    our_animal = Animal(arml=arml,legl=legl,neyes=neyes,tail=tail,furry=furry)

    #print out information about
    #our animal
    our_animal.print()


#executes the main function
if __name__=="__main__":
    main()