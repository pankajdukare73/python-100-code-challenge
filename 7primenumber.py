#Check number is prime or not
num=int(input("Enter the number to check to this prime or not:"))
flag=0
for i in range(2,num):
    if(num%i==0):
        flag=1
        break
if flag==0:
    print("The number",num,"is prime")
else:
    print("The number",num,"is not prime")

"""
Author:pankaj dukare
Output:
    Enter the number to check to this prime or not:37
    The number 37 is prime

    Enter the number to check to this prime or not:45
    The number 45 is not prime
"""