#This program will write 
#the sum, difference, and 
#product of different numbers.


#This function tells the 
#computer to print the sum
#of two floating point numbers
#and the answer's data type.
def PrintSum():
    xfloat = float(input("Enter first float to add : "))
    yfloat = float(input("Enter second float to add: "))
    mysum =  xfloat + yfloat
    print("Sum: ", mysum )
    print("data type: ", type(mysum))


#This function tells the 
#computer to print the difference
#between two integers
#and the answer's data type.
def PrintDifference():
    xint = int(input("Enter the first integer to subtract: "))
    yint = int(input("Enter the second integer to subtract: "))
    mydifference = xint - yint
    print("Difference: ", mydifference)
    print("data type: ", type(mydifference))


#This function tells the 
#computer to print the product
#of a floating point number and an integer
#and the answer's data type.
def PrintProduct():
    afloat = float(input("Enter the float to multiply: "))
    bint = int(input("Enter the integer to multiply: "))
    myproduct = afloat * bint
    print("Product:", myproduct)
    print("data type: ", type(myproduct))


#This defines our main()
#function for our program
def main():
    PrintSum()
    PrintDifference()
    PrintProduct()


#When we run the program,
#this executes first
if __name__=="__main__":
    main()