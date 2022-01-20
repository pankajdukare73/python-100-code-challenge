#fined the factorial of number
num=int(input("Enter the number to fined factorial of it:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("the factorial of number {0} is {1}".format(num,fact))

"""
Author:pankaj dukare
Output:
    Enter the number to fined factorial of it:5
    the factorial of number 5 is 120
"""