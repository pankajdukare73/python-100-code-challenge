#check the number is automorphic
#number whose square end in the same digits as the number itself.
num=int(input("Enter the number to check is Automorphic or not:"))
temp=num
pow=num*num
while(num>0):
    ndigit=num%10
    pdigit=pow%10
    if ndigit==pdigit:
        num=num//10
        pow=pow//10
        continue
    else:
        break
if num<=0:
    print("The number",temp,"is Automorphic number.")
else:
    print("The number",temp,"is not Automorphic number.")
"""
Author:pankaj dukare
Output:
    Enter the number to check is Automorphic or not:25
    The number 25 is Automorphic number.

    Enter the number to check is Automorphic or not:100
    The number 100 is not Automorphic number.
"""