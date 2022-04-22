#This program will define a function that returns x**3 + 8
#and then calls it using x = 9



#This function tells the computer
#to return x**3 + 8
def f(x):
    return x**3 + 8


#This defines the main function
def main():
    x = 9                    #set x = 9
    print("f(9) = ", f(x))   #call f(x) if x = 9 and prints the result
    if(f(x)>27):             #True if f(9) is greater than 27
        print("YAY!")


#executes the main function
if __name__=="__main__":
    main()