#Fined the power of number
#define the function to fined power to number
def powofnum(a,b):
    pownum=a**b
    print("the power of number {0} to {1} is {2}".format(a,b,pownum))

number=int(input("Enter Number to fined power:"))
pow=int(input("Enter Power to fined:"))
powofnum(number,pow) #call the function and pass argument as number and its power

"""
Author:pankaj dukare
Output:
    Enter Number to fined power:9 
    Enter Power to fined:3
    the power of number 9 to 3 is 729
"""