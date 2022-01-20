#positive or negative number
num=int(input("Enter number to check the number is positive or negative:"))
if num==0:
    print("Your Enter",num,"zero is not positive or negative.")
elif num>0:
    print("Your Enter",num,"this is positive Number.")
else:
    print("Your Enter",num,"this is negative Number.")

"""
Author:pankaj dukare
output:
    Enter number to check the number is positive or negative:45
    Your Enter 45 this is positive Number.

    Enter number to check the number is positive or negative:-356
    Your Enter -356 this is negative Number.

    Enter number to check the number is positive or negative:0
    Your Enter 0 zero is not positive or negative.
"""
